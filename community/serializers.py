from rest_framework import serializers
from .models import Community,Article,Comment
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        exclude = ('article',)
        # read_only = ('article',)


## 간략화 된 아티클 정보 불러오는 용도
class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    like_users_count =serializers.SerializerMethodField(read_only=True)
    def get_like_users_count(self,article):
        return article.like_users.count()

    class Meta:
        model = Article
        fields = '__all__'

### article을 생성하기 위해 쓰는 용도
class ArticleSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        exclude = ['like_users',]
        read_only = ('created_at','updated_at')

class UserArticleListSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(required=False)
    class Meta:
        model = Article
        fields = ['id','community','title','created_at']

class LikeUserSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True)
    class Meta:
        model = Article
        fields = ['id','title','like_users']
        read_only = ('created_at','updated_at')


class LikeArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['user','content','community']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only = ('created_at',)

