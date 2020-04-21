# 0421_workshop 

### 1. Model

```python
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

```

### 2. views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form=CommentForm()
    context = {
        'article': article,
        'form':form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request,article_id):
    if request.method=='POST':
        form=CommentForm(request.POST)
        article=get_object_or_404(Article,id=article_id)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.article=article
            comment.save()

    return redirect('articles:detail',article_id)

def comment_delete(request,article_id,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('articles:detail',article_id)
```

### 3.forms.py

```python
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content',]
```

