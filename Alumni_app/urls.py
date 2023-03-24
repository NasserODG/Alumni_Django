from django import views
from account import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('connexion.urls')),
    path('home/', include('home.urls')),

    path('', include('account.urls')),
]
