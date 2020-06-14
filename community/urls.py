from django.urls import path
from . import views

urlpatterns = [
    path('<int:community_rank>',views.communityList),
    path('articles/',views.articlelist),
    path('articles/<int:community_id>/',views.articlecreate),
]