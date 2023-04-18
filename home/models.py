from django.db import models
from account.models import CustomUser

class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='publications')

class Commentaire(models.Model):
    auteur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='commentaires')
    contenu = models.TextField()