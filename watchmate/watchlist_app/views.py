from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies':list(movies.values())
    }
    return JsonResponse(context)

def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
    }
    return JsonResponse(context)