from django.contrib import admin
from .models import Publication, Commentaire

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'publication', 'contenu')