from rest_framework import serializers
from .models import Movie,Genre,MovieRank


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
 

class MovieRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRank
        fields = '__all__'
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['movie'] = MovieListSerializer(instance.movie).data
    #     return response

class MovieDetailSerializer(serializers.ModelSerializer):
    movierank = MovieRankSerializer(many=True,read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
    