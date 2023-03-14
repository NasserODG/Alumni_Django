from django import forms

from connexion.models import Etudiant

class RegisterForm(forms.ModelForm):
    class Meta :
        model =Etudiant
        fields ={'first_name','last_name','email','phone_number','address','mot_de_passe'}
        widgets={
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control'}), 
        }