from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    db_id = models.TextField(primary_key=True)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
    # def __unicode__(self):
        # return self.db_id



class Movie(models.Model):
    # db_id = models.TextField(primary_key=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField(blank=True)
    original_language = models.CharField(max_length=10)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100, default='')
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_user')
    rate = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rate_user', through='UserRateMovie')
    rate_value = models.IntegerField(default=0)


class UserRateMovie(models.Model):
    value = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie, related_name='rated_movie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rated_user', on_delete=models.CASCADE)

