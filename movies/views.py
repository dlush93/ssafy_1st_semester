from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Genre
import random
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_cnt = len(page_obj)%3
    context = {
        'movies':movies,
        'page_obj':page_obj,
        'page_cnt':page_cnt
        
    }

    return render(request,'movies/index.html',context)

def like(request,movie_id):
    user = request.user
    movie = get_object_or_404(Movie,id=movie_id)
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
        status = False
    else:
        movie.like_users.add(user)
        status = True

    context = {
        'status':status,
        'like_count': movie.like_users.count(),
    }

    return JsonResponse(context)

def recommand(request):
    genres = Genre.objects.all()

    context = {
        'genres': genres,
    }
    return render(request,'movies/recommand.html',context)

def recommand_genre(request,genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movies.order_by('-vote_average').order_by('-popularity')[:10]
    context = {
        'movies':movies,
        'genre':genre
    }
    
    return render(request,'movies/recommand_genre.html',context) 



def recommand_genre_random(request):
    genres = list(Genre.objects.all().values('id'))
    genre_list=[]
    for genre in genres:
        genre_list.append(genre['id'])
    go_to = random.choice(genre_list)
    while True:
        genre = Genre.objects.get(id=go_to)
        movies = genre.movies.order_by('-vote_average').order_by('-popularity')[:10]
        if movies:
            break
        go_to = random.choice(genre_list)
    context={
        'movies':movies,
        'genre':genre
    }
    return render(request,'movies/recommand_genre.html',context) 

def recommand_random(request):
    movies_id = Movie.objects.all().values('id')
    movie_list=[]
    for movie in movies_id:
        movie_list.append(movie['id'])
    movie_choices = random.sample(movie_list,10)
    movies = []
    for movie_id in movie_choices:
        movies.append(Movie.objects.get(id=movie_id))
    context = {
        'movies':movies
    }
    return render(request,'movies/recommand_random.html',context)
