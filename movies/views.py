from django.shortcuts import render
from .models import Movie,Genre
from .serializers import MovieListSerializer,GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

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