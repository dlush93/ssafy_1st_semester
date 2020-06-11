from django.shortcuts import render
from .models import Movie,Genre
from .serializers import MovieListSerializer,GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)
