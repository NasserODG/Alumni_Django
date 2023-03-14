from django.db import models

# Create your models here.
class Etudiant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    is_active= models.BooleanField(default=False)
    mot_de_passe = models.CharField(max_length=12)
      

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