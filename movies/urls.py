from django.urls import path
from . import views

app_name = 'movies'


urlpatterns =[
    path('',views.index,name="index"),
    path('<int:movie_id>/like/',views.like,name="like"),
    path('recommand/',views.recommand,name="recommand"),
    path('recommand/<int:genre_id>/',views.recommand_genre,name="recommand_genre"),
    
]