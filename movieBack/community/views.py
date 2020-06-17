from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer


@api_view(['GET'])
def movie_articles_list(request, movie_pk):
    print("꺄륵")
    articles = Article.objects.filter(movie=movie_pk).all()
    print(articles)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)



@api_view(['GET'])
def article_comments(request, movie_pk, article_pk):
    print("아")
    comments = Comment.objects.filter(article=article_pk)
    print(comments)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_like(request):
#     movie = get_object_or_404(Movie, pk=request.data['id'])
#     if movie.like.filter(pk=request.user.pk).exists():
#         movie.like.remove(request.user)
#     else:
#         movie.like.add(request.user)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    print(request)
    serializer = ArticleSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    print(request.user)
    serializer = CommentSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)