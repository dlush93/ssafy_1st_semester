from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import FollowerSerializer,UserGradeSerializer
from community.serializers import LikeArticleListSerializer,ArticleListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
def follows(request,username):
    User = get_user_model()
    target_user = User.objects.get(username=username)
    serializer = FollowerSerializer(target_user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def grade(request,username):
    """
    회원의 등급을 올려주는 로직입니다.
    ---
    Header에 관리자의 토큰을 넣고 username에 등급을 올리고싶은 username을 넣어보세요. 관리자만 접근가능합니다.
    """
    if request.user.is_superuser:
        User = get_user_model()
        grade_user = User.objects.get(username=username)
        if grade_user.grade == 0:
            grade_user.grade +=1
            grade_user.save()
            serializer = UserGradeSerializer(grade_user)
            return Response(serializer.data)
        else:
            return Response({'message':'등업에 실패하셨습니다.'})
    else:
        return Response({'message':'관리자계정이 아닙니다.'})

@api_view(['GET'])
def like_article(reqeust,username):
    """
    해당 회원이 좋아요를 누른 게시글을 알수 있는 로직입니다.
    ---
    username에 알고싶은 회원의 이름을 넣어보세요.
    """
    User = get_user_model()
    liked_user = User.objects.get(username=username).like_articles.all()
    serializer = LikeArticleListSerializer(liked_user,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user(request):
    """
    회원의 등급을 알 수 있는 곳입니다.
    ---
    Header에 토큰을 넣어 확인해보세요
    """

    User = get_user_model()
    try:
        user_info = User.objects.get(username = request.user.username)
    except:
        return Response({'message':'없는 사용자입니다.'})
    serializer = UserGradeSerializer(user_info)
    return Response(serializer.data)

@api_view(['GET'])
def user_article(reqeust,username):
    """
    해당 회원이 작성한 글을 알 수 있는 곳입니다..
    ---
    username에 해당회원의 이름을 넣고 GET 요청을 보내보세요
    """
    User = get_user_model()
    target_articles = User.objects.get(username = username).article.all()
    serializers = ArticleListSerializer(target_articles,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def user_total_profile(reqeust,username):
    """
    회원에 대한 프로필을 간략적으로 알 수 있는 곳입니다.
    ---
    username을 넣어보세요. 회원의 등급,작성글 수 등을 알 수있습니다.
    """


    User = get_user_model()
    target_user = User.objects.get(username = username)
    grade = '준회원'
    if target_user.is_superuser:
        grade = "관리자"
    else:
        if target_user.grade:
            grade = "정회원"
    user_article = target_user.article.all()
    received_count = 0
    for article in user_article:
        received_count += article.like_users.all().count()
    article_count = target_user.article.all().count()
    comment_count = target_user.comment.all().count()
    rank_count = target_user.movierank_set.all().count()
    like_count = target_user.like_articles.all().count()

    serializer = {
        'grade':grade,
        'article_count':article_count,
        'comment_count':comment_count,
        'rank_count' : rank_count,
        'received_count' : received_count,
        'like_count': like_count,
    }
    return Response(serializer)