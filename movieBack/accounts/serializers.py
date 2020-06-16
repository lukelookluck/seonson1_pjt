from django.contrib.auth import get_user_model
from rest_framework import serializers
from movies.serializers import MovieSerializer, UserRateMovieSerializer
from community.serializers import ArticleSerializer, CommentSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    like_user = MovieSerializer(many=True, read_only=True)
    rate_user = MovieSerializer(many=True, read_only=True)
    rated_user = UserRateMovieSerializer(read_only=True)
    like_articles = ArticleSerializer(many=True, read_only=True)
    dislike_articles = ArticleSerializer(many=True, read_only=True)
    comments = CommentSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #     return User(**validated_data)

    # def update(self, instance, validated_data):
    #     print(validated_data.get('like_movie'))
    #     instance.like_movie.append(validated_data.get('like_movie'))
    #     instance.save()
    #     return instance