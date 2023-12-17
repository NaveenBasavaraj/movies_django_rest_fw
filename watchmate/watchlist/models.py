from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Stream(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name+': '+self.about

class WatchList(models.Model):
    
    title = models.CharField(max_length=200)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='watchlist')

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return str(self.watchlist.title)+': '+ str(self.rating*'*')
    