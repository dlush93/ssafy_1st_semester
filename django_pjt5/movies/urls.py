from django.urls import path
from . import views

app_name = 'movies'


urlpatterns =[
    path('',views.index,name="index"),
    path('<int:movie_id>/like/',views.like,name="like"),
    path('recommand/',views.recommand,name="recommand"),
    path('recommand/<int:genre_id>/',views.recommand_genre,name="recommand_genre"),
    path('recommand/genre_random/',views.recommand_genre_random,name="recommand_genre_random"),
    path('recommand/random/',views.recommand_random,name="recommand_random")
    
]