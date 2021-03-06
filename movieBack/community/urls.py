from django.urls import path
from . import views

app_name = "community"

urlpatterns =[
    # path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/comment_create/', views.comment_create, name="comment_create"),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/articles/', views.movie_articles_list, name='movie_articles_list'),
    path('<int:movie_pk>/<int:article_pk>/comments', views.article_comments, name='article_comments'),

]