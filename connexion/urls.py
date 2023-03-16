from django.urls import path

from . import views

urlpatterns = [
    path('', views.connexion.as_view(), name='connexion'),
]