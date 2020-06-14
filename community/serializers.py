from rest_framework import serializers
from .models import Community,Article,Comment
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleShow_in_Community_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['community']

class CommunityListSerializer(serializers.ModelSerializer):
    article = ArticleShow_in_Community_Serializer(many=True)
    class Meta:
        model = Community
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    community = CommunitySerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        exclude = ['like_users',]
        read_only = ('created_at','updated_at')