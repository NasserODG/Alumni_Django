from django import forms  
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    nom = forms.CharField(max_length=30, required=False, help_text='Required.')
    prenom = forms.CharField(max_length=30, required=False, help_text='Required.') 
    class Meta:  
        model = CustomUser  
        fields = ('username','nom','prenom', 'email', 'password1', 'password2')
        
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)