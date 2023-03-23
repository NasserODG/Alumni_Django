from django import forms  
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = CustomUser  
        fields = ('username', 'email', 'password1', 'password2')
        
        
# class LoginForm(AuthenticationForm):  
#     username = forms.CharField(max_length=200, help_text='Required')  
#     class Meta:  
#         model = User  
#         fields = ('username', 'password')