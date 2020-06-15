from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import FollowerSerializer,UserGradeSerializer
from community.serializers import LikeArticleListSerializer
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
    User = get_user_model()
    liked_user = User.objects.get(username=username).like_articles.all()
    serializer = LikeArticleListSerializer(liked_user,many=True)
    return Response(serializer.data)
