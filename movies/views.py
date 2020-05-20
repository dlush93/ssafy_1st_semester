from django.shortcuts import render,get_object_or_404,redirect
from .models import Movie
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Genre
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':movies,
        'page_obj':page_obj,
        'page_number':page_number,
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
    movies = Genre.objects.get(id=genre_id).movies.order_by('-vote_average').order_by('-popularity')[:10]
    context = {
        'movies':movies
    }
    
    return render(request,'movies/recommand_genre.html',context) 




