from django.urls import path
from . import views
urlpatterns = [
    #### following followers 목록
    path('follows/<username>/',views.follows),
    #### 회원등급을 올려주는 거 (admin 계정만 올수 있다.)
    path('grade/<username>/',views.grade),
    #### 해당 회원의 좋아하는 게시글들 ####
    path('like_article/<username>/',views.like_article),
    #### 회원 등급 가져오기
    path('',views.user),
    ### 해당회원의 작성글
    path('articles/<username>/',views.user_article),
    #### 회원 profile 정보들
    path('profile/<username>/',views.user_total_profile)
]
