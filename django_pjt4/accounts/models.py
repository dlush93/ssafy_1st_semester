from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followings')



######
### 0. 인덱스
## 1. 회원가입  ->
## 2. 로그인   ->
## 3. 로그아웃 ->
## 4. 디테일 페이지  메인url/accounts/{사용자 이름}/ ->
## 5. 팔로우