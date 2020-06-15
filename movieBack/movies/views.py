from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()[:5]

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
    print(request.data['id'])
    # request.data['like'] = request.user
    movie = get_object_or_404(Movie, pk=request.data['id'])
    if movie.like.filter(pk=request.user.pk).exists():
        movie.like.remove(request.user)
        liked = False
    else:
        movie.like.add(request.user)
        liked = True
    
    context = {
        'liked': liked,
        'like_user_count': request.user.like_user.count(),
        'like_count': movie.like.count(),
    }

    return Response(context)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(data = request.data['id'])
    #     return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_genre_connect(request):
    serializer = MovieSerializer(instance=request.data, data=request.data, partial=True)
    print("request.data", request.data)
    if serializer.is_valid(raise_exception=True):
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
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

