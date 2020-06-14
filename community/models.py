from django.db import models
from django.conf import settings
# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='article')
    Community = models.ForeignKey(Community,on_delete=models.CASCADE,related_name='article')
    like_users = models.ManyToManyFiled(settings.AUTH_USER_MODEL,related_name='like_articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')

