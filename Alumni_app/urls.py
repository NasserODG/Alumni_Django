from django import views
from connexion import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('connexion/', include('connexion.urls')),
    path('register/', include('register.urls')),
]
