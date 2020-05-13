from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)

@login_required
def create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('movies:index')
        else:
            form = MovieForm()
        context ={
            'form':form
        }
        return render(request,'movies/form.html',context)
    else:
        messages.warning(request,'잘못된 접근입니다.')
        return redirect('movies:index')


def detail(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    context ={
        'movie':movie
    }
    return render(request,'movies/detail.html',context)


def update(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST,instance = movie)
            if form.is_valid():
                review=form.save()
                return redirect('movies:detail',movie.id)

        else:
            form = MovieForm(instance = movie)
        context = {
            'form':form
        }
        return render(request,'movies/form.html',context)
    else:
        messages.warning(request,'잘못된 접근입니다.')
        return redirect('movies:index')


def delete(request,movie_id):
    if request.user.is_superuser:
        movie = get_object_or_404(Movie,id=movie_id)
        movie.delete()
        return redirect('movies:index')
    else:
        messages.warning(request,'잘못된 접근입니다.')
        return redirect('movies:index')