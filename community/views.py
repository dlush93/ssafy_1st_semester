from django.shortcuts import render
from .serializers import ArticleListSerializer,ArticleSerializer,CommunityListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article,Community
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
def articlelist(request):
    articles = Article.objects.all()
    serializers = ArticleListSerializer(articles,many=True)
    return Response(serializers.data)
    
@api_view(['GET'])
def communityList(request,community_rank):
    community_article =  Community.objects.get(rank=community_rank).article.all()
    serializers = ArticleListSerializer(community_article,many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articlecreate(request,community_id):
    temp = request.data['content']
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(community_id=community_id,user=request.user)
        return Response(serializer.data)