from django.urls import path

from account.views import index , signup, activate, login_request


urlpatterns = [  
    path('', index, name = 'index'),  
    path('register/', signup , name='signup'), 
    path('activate/<uidb64>/<token>/',activate, name='activate'),  
    path("login", login_request, name="login")
] 