from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import json

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
                movie=form.save(commit=False)
                url = f'https://api.themoviedb.org/3/search/movie?api_key=69570904cbfa7d422a8a753a576d8c32&language=ko-KR&query={movie.title}&page=1&include_adult=false2'
                res= requests.get(url)
                js =  json.loads(res.text)
                re = js['results'][0]['poster_path']
                movie.poster = f'https://image.tmdb.org/t/p/w300{re}'
                movie.save()
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