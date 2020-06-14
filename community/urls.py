from django.urls import path
from . import views

urlpatterns = [
    #### 커뮤니티 정보
    path('',views.List),
    ### 커뮤니티별 게시글
    path('<int:community_id>',views.communityList),
    # 게시글 만드는 과정
    path('/<int:community_id>/articles',views.articlecreate),
    ### 모든 게시글 가저오는거
    path('articles/',views.articlelist),
]