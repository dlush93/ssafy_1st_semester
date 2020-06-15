from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #### Movie에 대한 전체적인 표현
    path('<int:movie_id>/',views.MovieDetail),
    #### MOVIE에 평점 만드는 곳
    path('<int:movie_id>/comments/',views.CommentCreate),
    #### Movie에 평점 삭제하는 곳
    path('comments/<int:comment_id>/',views.CommentDelete)
]


