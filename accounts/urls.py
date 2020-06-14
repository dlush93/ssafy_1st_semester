from django.urls import path
from . import views
urlpatterns = [
    path('follows/<username>/',views.follows)
]