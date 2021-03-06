from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('<int:num>/', views.movies_list, name='movies_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('genre_create/', views.genre_create, name='genre_create'),
    # path('connect/', views.movie_genre_connect, name='movie_genre_connect'),
    # path('<int:movie_pk>/update/', views.update, name='update'),
    # path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('like/', views.movie_like, name='movie_like'),
    path('rate/', views.rate_movie, name='rate_movie'),
    path('recomand/<int:num>/', views.movie_recomand, name='movie_recomand'),
    path('recomand2/', views.movie_recomand2, name='movie_recomand2'),
    path('get_value/<int:user_pk>/<int:movie_pk>/', views.get_user_movie_rate_value, name='get_user_movie_rate_value'),
]