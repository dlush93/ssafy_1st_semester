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

### 2. Comment Create

```python
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
```

### 3. Comment Read

```python
	{% for comment in article.comment_set.all %}
		댓글 번호 : {{ forloop.counter}}
		댓글 목록 : {{ comment.content }}
		<a href="{% url 'articles:comment_delete' article.pk comment.pk %}">댓글삭제</a>
		<hr>

	{% endfor %}
```

### 4. Comment Delete 

```python
def comment_delete(request,article_id,comment_id):
    if request.method=='POST'
        comment=Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect('articles:detail',article_id)
```

