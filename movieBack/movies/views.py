from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, UserRateMovieSerializer


@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()[:20]

    # if request.user.is_authenticated:
    #     if request



    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_create(request):
    serializer = MovieSerializer(data=request.data)
    print("+++++++++++++++++++++++++", request.data.get('genre_ids'))
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request):
    movie = get_object_or_404(Movie, pk=request.data['id'])
    if movie.like.filter(pk=request.user.pk).exists():
        movie.like.remove(request.user)
    else:
        movie.like.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_movie(request):
    user = request.data
    user['user'] = request.user.id
    serializer = UserRateMovieSerializer(data=user)
    print("request.data", user)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        print('asdas')
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genre_create(request):
    serializer = GenreSerializer(data=request.data)
    print(request.data.get('id'))
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    article = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(article)
    return Response(serializer.data)

