from watchlist.models import WatchList, Stream
from django.http import JsonResponse
from watchlist.api.serializers import WatchListSerializer, StreamSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from watchlist.api.permissions import IsAdminToPost


class WatchListAV(APIView):
    permission_classes = [IsAdminToPost]
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchDetailAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)
    
class StreamListAV(APIView):
    def get(self, request):
        streams = Stream.objects.all()
        serializer = StreamSerializer(streams, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StreamDetailAV(APIView):
    def get(self, request, pk):
        try:
            stream = Stream.objects.get(id=pk)
        except Stream.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamSerializer(stream,  context={'request':request})
        return Response(serializer.data)
    
    def delete(self, request, pk):
        stream = Stream.objects.get(id=pk)
        stream.delete()
        return Response(status=status.HTTP_200_OK)

        
            
        