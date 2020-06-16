from rest_framework import serializers
from .models import Genre, Movie, UserRateMovie
from accounts.models import User
# from accounts.serializers import UserSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        # read_only_fields = ('db_id',)

    
class UserRateMovieSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = UserRateMovie
        fields = '__all__'
        # read_only_fields = ('user', )
    # def create(self, validated_data):
    #     return UserRateMovie.objects.create(**validated_data)


class MovieSerializer(serializers.ModelSerializer):
    # genre_ids = serializers.StringRelatedField(many=True)
    genre_ids = GenreSerializer(many=True, read_only=True)
    rated_movie = UserRateMovieSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like', 'rate', )