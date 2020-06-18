from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Genre, Movie, UserRateMovie
from .serializers import GenreSerializer, MovieSerializer, UserRateMovieSerializer
from django.core import serializers
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movies_list(request, num):
    print("꺄륵")
    print(num)
    A = (num) * 20
    B = (num + 1) * 20
    # 유저가 좋아요한 영화들 쿼리셋
    temp_list = request.user.rate_user.values('id')

    movies = Movie.objects.filter(~Q(id__in=temp_list)).all()[A:B]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_create(request):
    serializer = MovieSerializer(data=request.data)
    print("+++++++++++++++++++++++++", request.data.get('genre_ids'))
    print(serializer)
    if serializer.is_valid(raise_exception=False):
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
    a = UserRateMovie.objects.filter(user=request.user.id, movie=request.data['movie'])
    print(a)
    if a:
        a.delete()

    user = request.data
    user['user'] = request.user.id
    serializer = UserRateMovieSerializer(data=user)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genre_create(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    article = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(article)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_recomand(request, num):
    
    if request.user.rated_user.count():
        # 유저가 좋아요한 영화들 쿼리셋
        temp_list = request.user.rated_user.filter(value__gte=3).values('movie')

        temp_genres = Genre.objects.filter(movies__in=temp_list).values('db_id')
        # 그 장르들이 있는 영화들의 쿼리셋 중 랜덤으로 10개
        temp_movies = Movie.objects.filter(genre_ids__in=temp_genres).order_by('?')[:10]

    else:
        temp_movies = Movie.objects.order_by('?')[:10]

    print(temp_movies)

    serializer = MovieSerializer(temp_movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_recomand2(request):
    if request.user.rated_user.count():
        # 사용자가 3점 이상 준 영화들 쿼리셋
        temp_list = request.user.rated_user.filter(value__gte=3).values('movie')
        # 그 장르에 3점 이상 준 유저들 쿼리셋
        temp_user = UserRateMovie.objects.filter(movie__in=temp_list, value__gte=3).values('user')
        # 그 유저들이 3점 이상 준 영화 목록들 중 사용자가 평가하지 않은 영화들 id 쿼리셋
        temp_movies2 = UserRateMovie.objects.filter(Q(user__in=temp_user) & Q(value__gte=3) & ~Q(movie__in=temp_list)).values('movie')
        # 찾은 영화들 id 쿼리셋에 해당되는 영화들 쿼리셋
        temp_movies = Movie.objects.filter(id__in=temp_movies2)[:10]

    else:
        temp_movies = Movie.objects.order_by('?')[:10]

    print(temp_movies)

    serializer = MovieSerializer(temp_movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_movie_rate_value(request, user_pk, movie_pk):
    value = UserRateMovie.objects.filter(user=user_pk, movie=movie_pk).all()

    print(value)
    serializer = UserRateMovieSerializer(value, many=True)
    return Response(serializer.data)