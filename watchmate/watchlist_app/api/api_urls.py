from django.urls import path
from watchlist_app.api.views_functions import * # function based
from watchlist_app.api.views_class import * # class based

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_details'),
    
    # Function based views
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_details'),
]