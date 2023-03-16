from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Etudiant(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=12)
    is_active= models.BooleanField(default=False)
      

    class Meta :
        ordering = ['first_name', 'last_name']
        verbose_name = 'Etudiant'
        verbose_name_plural='Etudiants'
    def __str__(self):
        return self.first_name
                
        
class Connexion(models.Model):
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=12)
    
    def __str__(self):
        return str(self.email)