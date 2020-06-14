from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.order_by('-pk')
    serializer = MovieSerializer(Movie, many=True)
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

