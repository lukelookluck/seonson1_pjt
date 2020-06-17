from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('like/', views.like, name='like'),
    path('get_username/', views.get_username, name='get_username'),
]