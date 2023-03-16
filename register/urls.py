from django.urls import path

from connexion import views
from .views import (sign_up,log_out,activate);

urlpatterns = [
    path('',sign_up, name='sign_up'),
    path('deconnexion',log_out, name='log_out'),
    path('active/(?P<uidb64>[0-9]+)/(?P<token>[^/]+)\\Z' , activate , name='activate'),
]
