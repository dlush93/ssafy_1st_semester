from django.db import models

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=100)
    movie_title=models.CharField(max_length=30)
    rank=models.IntegerField(default=0)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
