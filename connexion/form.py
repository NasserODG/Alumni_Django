from django import forms

from connexion.models import Etudiant, Connexion

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = Connexion
        fields = ('email', 'mot_de_passe')
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control'}),
        }