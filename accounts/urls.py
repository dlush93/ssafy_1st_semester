from django.urls import path
from . import views
urlpatterns = [
    #### following followers 목록
    path('follows/<username>/',views.follows),
    #### 회원등급을 올려주는 거 (admin 계정만 올수 있다.)
    path('grade/<username>/',views.grade),
    #### 해당 회원의 좋아하는 게시글들 ####
    path('like_article/<username>/',views.like_article),
    path('<username>/',views.user),
]
