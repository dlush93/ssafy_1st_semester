from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_reviews')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    review = models.ForeignKey(Review,on_delete = models.CASCADE)