from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Check watchlist_app.views for pure function based views without serializers

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)