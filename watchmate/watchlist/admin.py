from django.contrib import admin
from watchlist.models import WatchList, Stream, Review
# Register your models here.

admin.site.register(WatchList)
admin.site.register(Stream)
admin.site.register(Review)