from django import forms
from home.models import Commentaire

class CommentaireForm(forms.ModelForm):
    contenu = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50,'class': 'form-control'}), max_length=500)

    class Meta:
        model = Commentaire
        fields = ['contenu']
