from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.models import CustomUser
from home.form import CommentaireForm
from home.models import Publication, Commentaire


from django.utils import timezone



def index(request):
    publications = Publication.objects.all()
    commentaires = Commentaire.objects.all()
    context = {
        'publications': publications,
        'commentaires': commentaires,
    }
    return render(request, 'home.html', context)


# def pub(request):
#     publications = Publication.objects.all()
#     context = {
#         'publications': publications,
#     }
#     return render(request, 'toutes_publications.html', context)

@login_required
def add_Comment(request, publication_id):
    publication = Publication.objects.get(id=publication_id)
    commentaires = Commentaire.objects.filter(publication=publication).all()

    
    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        user = CustomUser.objects.get()
        commentaire = Commentaire.objects.create(publication = publication,auteur = user,contenu=contenu)
            # commentaire = form.save(commit=False)
        commentaire.save()
            # commentaire.
            # commentaire.
            # commentaire.save()
        return render(request, 'detail_publication.html')
            
    context = {
        'publication': publication,
        'commentaires': commentaires,
        'publication_id':publication_id
    }
    return render(request, 'detail_publication.html', context)


def detail_pub(request, publication_id):
    return render(request, 'detail_publication.html')