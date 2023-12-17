from rest_framework import serializers
from watchlist.models import WatchList, Stream, Review

# using model serializers
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
    
    def get_len_names(self, object):
        return len(object.title)
        

class StreamSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(many=True, 
                                                    read_only=True,
                                                    view_name='stream_details')
    class Meta:
        model = Stream
        fields = ['name', 'about', 'watchlist']


# class StreamSerializer(serializers.ModelSerializer):
#     # watchlist = WatchListSerializer(many=True, read_only=True)
#     watchlist = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Stream
#         fields = "__all__"
    