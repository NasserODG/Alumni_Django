from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion', views.connexion.as_view(), name='connexion'),
]