# 0407 exercise

- views.py

  ```python
  from django.shortcuts import render,redirect,get_object_or_404
  from .models import Article
  from .forms import ArticleForm
  # Create your views here.
  def index(request):
      articles=Article.objects.order_by('-id')
      context={
          'articles':articles,
      }
      return render(request,'articles/index.html',context)
  
  def create(request):
      if request.method =='POST':
          form=ArticleForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
  
      else:
          form=ArticleForm()
          context={
              'form':form,
          }
          return render(request,'articles/create.html',context)
  
  def detail(request,id):
      article=get_object_or_404(Article,id=id)
      context={
          'article':article
      }
      return render(request,'articles/detail.html',context)
  ```
- forms.py
	
	```python
	from django import forms
	from .models import Article
	
	class ArticleForm(forms.ModelForm):
	    class Meta:
	        model=Article
	        fields='__all__'
	```





# 결과 사진

- READ

  ![image-20200407162158410](0407_exercise.assets/image-20200407162158410.png)

- CREATE

  ![image-20200407162301888](0407_exercise.assets/image-20200407162301888.png)

- DETAIL

  ![image-20200407162341251](0407_exercise.assets/image-20200407162341251.png)