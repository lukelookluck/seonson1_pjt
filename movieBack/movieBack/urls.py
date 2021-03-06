from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls.')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('movies/', include('movies.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls'))
]
