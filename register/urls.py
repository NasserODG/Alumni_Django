from django.urls import path
from .views import (
    home,sign_in,sign_up,log_out,activate);

urlpatterns = [
    path('',home, name='register'),
    path('register',sign_up, name='sign_up'),
    path('connexion',sign_in, name='sign_in'),
    path('deconnexion',log_out, name='log_out'),
    path('active/<int:uidb64>/<token>' , activate , name='activate'),
]
