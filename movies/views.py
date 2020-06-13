from django.shortcuts import render
from .models import Movie,Genre,MovieRank
from .serializers import MovieListSerializer,GenreSerializer,MovieDetailSerializer,MovieRankSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination


from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(movies,request)
        serializer = MovieListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])

def MovieDetail(request,movie_id):
    if request.method == 'GET':
        print(request.user.is_superuser)
        movie = Movie.objects.filter(id=movie_id)
        serializer = MovieDetailSerializer(movie,many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CommentCreate(request,movie_id):    
    serializer = MovieRankSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_id,user=request.user)
        return Response(serializer.data)