from django.urls import path
from watchlist.api.views import *

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('streams/', StreamListAV.as_view(), name='stream_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_details'),
    path('streams/<int:pk>/', StreamDetailAV.as_view(), name='stream_details'),
]