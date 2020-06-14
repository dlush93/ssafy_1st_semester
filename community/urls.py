from django.urls import path
from . import views

urlpatterns = [
    path('articles/',views.articlelist),
    path('articles/<int:community_id>/',views.articlecreate),
]