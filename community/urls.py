from django.urls import path
from . import views

urlpatterns = [
    #### 커뮤니티 정보
    path('',views.List),
    ### 커뮤니티별 게시글
    path('<int:community_id>/',views.communityList),
    ### 게시글 만드는 과정
    path('<int:community_id>/articles/',views.articlecreate),
    ### 모든 게시글 가저오는거
    path('articles/',views.articlelist),
    ### 특정게시글 조회,수정,삭제
    path('articles/<int:article_id>/',views.articledetail),
    ### 해당 게시글을 좋아하는 유저들의 목록을 보여주는거
    path('like_users/<int:article_id>',views.likeusersList),
    ### 좋아요 하는 요청주소
    path('like/<int:article_id>',views.likeuser),
]

