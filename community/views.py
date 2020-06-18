from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import ArticleListSerializer,ArticleSerializer,CommunitySerializer,LikeUserSerializer,UserArticleListSerializer,CommentSerializer,CommentListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article,Community,Comment
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def articlelist(request):
    articles = Article.objects.all()
    serializers = ArticleListSerializer(articles,many=True)
    return Response(serializers.data)
cnt = 0
@api_view(['GET'])
def communityList(request,community_id):
    global cnt
    cnt +=1
    try:
        community_article =  Community.objects.get(id=community_id).article.all()
    except:
        return Response({'message':'해당페이지가 없습니다.'},status=status.HTTP_404_NOT_FOUND)
    serializers = ArticleListSerializer(community_article,many=True)
    print(cnt)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articlecreate(request,community_id):
    community_rank = Community.objects.get(id=community_id).rank
    ## 수정사항 슈퍼유저인지 판별해서 슈퍼유저이면 그냥 작성...
    if community_rank == request.user.grade or request.user.is_superuser:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community_id=community_id,user=request.user)
            return Response(serializer.data)
    else:
        return Response({'message':'접근권한이 없습니다.'})
        
@api_view(['GET'])
def List(request):
    community = Community.objects.all()
    serializers = CommunitySerializer(community,many=True)
    return Response(serializers.data)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def articlefunc(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return Response({'message':'해당페이지가 없습니다.'},status=status.HTTP_404_NOT_FOUND)
    if request.user == article.user:
        if request.method == 'PUT':
            serializer = ArticleSerializer(article,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':
            article.delete()
            return Response({ 'isStatus' : 'true',
                                'message':'성공적으로 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message':'허락된 사용자가 아닙니다.'},status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def articledetail(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return Response({'message':'해당페이지가 없습니다.'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

            
@api_view(['GET'])
def likeusersList(request,article_id):
    article = Article.objects.get(id=article_id)
    serializer = LikeUserSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likeuser(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return Response({'message':'해당 페이지가 없습니다.'})
    if article.user == request.user:
        return Response({ 'likestat': 0,
                'likestatus': False, 
            'message':'자기글에 추천할 수 없습니다.'})
    else:
        if article.like_users.filter(id=request.user.id).exists():
            article.like_users.remove(request.user)
            return Response({'message':'좋아요를 취소했습니다.',
            'likestat':-1,
            'likestatus':False})
        else:
            article.like_users.add(request.user)
            return Response({'message':'좋아요를 했습니다.',
            'likestat':1,
            'likestatus':True,})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def commentcreate(request,article_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user,article_id=article_id)
        return Response(serializer.data)

@api_view(['GET'])
def commentslist(request,article_id):
    comments = Article.objects.get(id=article_id).comment.all()
    serializers =CommentListSerializer(comments,many=True)
    return Response(serializers.data)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def commentfunc(request,comment_id):
    print('여기도 안오냐.?')
    try:
        comment = Comment.objects.get(id=comment_id)
    except:
        return Response({'message':'해당페이지가 없습니다.'},status=status.HTTP_404_NOT_FOUND)
    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentListSerializer(comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':
            comment.delete()
            return Response({ 'isStatus' : 'true',
                                'message':'성공적으로 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message':'허락된 사용자가 아닙니다.'},status=status.HTTP_403_FORBIDDEN)