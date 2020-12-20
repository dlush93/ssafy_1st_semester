from django.contrib import admin
from .models import Genre,Movie
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','popularity','vote_average')

admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MovieAdmin)