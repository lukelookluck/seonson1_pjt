from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('genre_create/', views.genre_create, name='genre_create'),
    path('connect/', views.movie_genre_connect, name='movie_genre_connect'),
    # path('<int:movie_pk>/update/', views.update, name='update'),
    # path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # path('<int:movie_pk>/like/', views.like, name='like'),
]