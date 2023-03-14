from django.contrib import admin

from connexion.models import Connexion, Etudiant

# Register your models here.
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email','phone_number','mot_de_passe')
    


admin.site.register(Connexion)
#admin.site.register(Etudiant)
