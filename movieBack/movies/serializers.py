from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name')


class MovieSerializer(serializers.ModelSerializer):
    geres = GenreSerializer

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ()