# 0608_workshop

- accounts/serializers.py

  ```python
  from rest_framework import serializers
  from django.contrib.auth import get_user_model
  
  User = get_user_model()
  class UserSeriailizer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ['id','username']
  ```

  

- articles/serializers.py

  ```python
  from .models import Article
  from rest_framework import serializers
  from accounts.serializers import UserSeriailizer
  
  class ArticleListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Article
          fields = ['id','title']
  
  
  class ArticleSerializer(serializers.ModelSerializer):
      user = UserSeriailizer(required=False)
      class Meta:
          model = Article
          fields = '__all__'
          read_only_fields =['id','created_at','user'] ## 수정불가 항목
  ```

  