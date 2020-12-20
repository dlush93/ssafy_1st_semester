from rest_framework import serializers
from .models import Movie,Genre,MovieRank
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class Movie_Show_in_MovieRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title']

class MovieRankSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    movie = Movie_Show_in_MovieRankSerializer(required=False)
    class Meta:
        model = MovieRank
        fields = '__all__'
        read_only = 'created_at'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['movie'] = MovieListSerializer(instance.movie).data
    #     return response

class MovieDetailSerializer(serializers.ModelSerializer):
    movierank = MovieRankSerializer(many=True,read_only=True)
    movierank_count =  serializers.SerializerMethodField(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    def get_movierank_count(self,movie):
        return movie.movierank.count()
    class Meta:
        model = Movie
        fields = '__all__'
    