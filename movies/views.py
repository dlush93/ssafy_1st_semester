from django.shortcuts import render
from .models import Movie,Genre,MovieRank
from .serializers import MovieListSerializer,GenreSerializer,MovieDetailSerializer,MovieRankSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[0:9]
        print(movies)
        # paginator = PageNumberPagination()
        # paginator.page_size = 10
        # result_page = paginator.paginate_queryset(movies,request)
        # return paginator.get_paginated_response(serializer.data)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def MovieDetail(request,movie_id):
    if request.method == 'GET':
        movie = Movie.objects.filter(id=movie_id)
        serializer = MovieDetailSerializer(movie,many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CommentCreate(request,movie_id):
    print(f'reqeuset.data:{request.data},request.POST:{request.POST}')    

    serializer = MovieRankSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_id,user=request.user)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def CommentDelete(request,comment_id):
    try:
        movierank = MovieRank.objects.get(id=comment_id)
    except:
        return Response({'message':'해당페이지가 없습니다.'},status=status.HTTP_404_NOT_FOUND)

    if request.user == movierank.user:
        if request.method == 'DELETE':
            movierank.delete()
            return Response({'message':'성공적으로 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': '잘못된 접근입니다.'})
    else:
        return Response({'message':'허락된 사용자가 아닙니다.'},status=status.HTTP_403_FORBIDDEN)