from rest_framework import serializers
from watchlist_app.models import Movie

# field level validation using validators
def desc_length(value):
    if len(value) <= 2:
        raise serializers.ValidationError("Description too short!!")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[desc_length])
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name should not match description")
        return data
    
    # field level validation
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name is too short!!")
        return value
        
        
    