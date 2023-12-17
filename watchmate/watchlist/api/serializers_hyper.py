from rest_framework import serializers
from watchlist.models import WatchList, Stream

# using hyper linked model serializers
class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    len_names = serializers.SerializerMethodField()
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
    