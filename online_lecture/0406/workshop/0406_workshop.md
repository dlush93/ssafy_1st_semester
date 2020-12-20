# 0406_workshop

## URL namespaces

### 요청 경로 및 이동 경로 수정

#### urls.py(수정 전)

```python
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('new/',views.new),
    path('create/',views.create),
    path('<int:id>/',views.detail),
    path('<int:id>/edit',views.edit),
    path('<int:id>/update',views.update),
    path('<int:id>/delete',views.delete)
]
```

#### urls.py(수정 후)

```python
from django.urls import path
from . import views
app_name='articles'
urlpatterns=[
    path('',views.index ,name="index"),
    path('new/',views.new ,name="new"),
    path('create/',views.create, name="create"),
    path('<int:id>/',views.detail, name="detail"),
    path('<int:id>/edit/',views.edit, name="edit"),
    path('<int:id>/update/',views.update, name="update"),
    path('<int:id>/delete/',views.delete ,name="delete")
]
```

#### views.py(수정 후)

```python
from django.shortcuts import render,redirect
from .models import Articles
# Create your views here.
def index(request):
    articles=Articles.objects.all()
    context={
        'articles':articles
    }
    return render(request,'articles/index.html',context)


def new(request):
    return render(request,'articles/new.html')

def create(request):
    article=Articles()
    article.title=request.GET.get('title')
    article.content=request.GET.get('content')
    article.save()
    # return render(request,'articles/create.html')
    return redirect('articles:index')

def detail(request,id):
    article=Articles.objects.get(id=id)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def edit(request,id):
    article=Articles.objects.get(id=id)
    context={
        'article':article,
    }
    return render(request,'articles/edit.html',context)

def update(request,id):
    article=Articles.objects.get(id=id)
    article.title=request.GET.get('title')
    article.content=request.GET.get('content')
    article.save()
    return redirect('articles:detail',article.id)

def delete(request,id):
    article=Articles.objects.get(id=id)
    article.delete()
    return redirect('articles:index')
```





### 요청 방식 변경

#### new.html(수정 후)

```html
{% extends 'base.html' %}

{% block body %}
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    TITLE:<input type="text" name="title"> <br>
    CONTENT: <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <br>
    <input type="submit" value="제출">
</form>

<a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

#### edit.html(수정 후)

```html
{% extends 'base.html' %}

{% block body %}
<h1>EDIT</h1>
<form action="/articles/{{ article.id }}/update/" method="POST">
    {% csrf_token %}
    TITLE:<input type="text" name="title" value="{{ article.title }}"><br>
    CONTENT:<textarea name="content" id="" cols="30" rows="10">{{ article.content }}
    </textarea><br>
    <input type="submit" value="수정">
</form>
<a href="/articles">BACK</a>
{% endblock %}
```

### views.py(수정 후)

```python
def create(request):
    article=Articles()
    article.title=request.POST.get('title')
    article.content=request.POST.get('content')
    article.save()
    # return render(request,'articles/create.html')
    return redirect('articles:index')
def update(request,id):
    article=Articles.objects.get(id=id)
    article.title=request.POST.get('title')
    article.content=request.POST.get('content')
    article.save()
    return redirect('articles:detail',article.id)
```

