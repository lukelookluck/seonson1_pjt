from django.db import models
from django.conf import settings
from movies.models import Movie

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    LIKE = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    DISLIKE = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_articles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default='')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)