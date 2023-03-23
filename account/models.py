from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=254)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    token = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','password','first_name', 'last_name']


    def __str__(self):
        return self.username
