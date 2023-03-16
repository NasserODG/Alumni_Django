from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login, logout

from connexion.form import ConnexionForm
from connexion.models import Connexion


def index(request):
    return render(request, 'index.html')

class connexion(SuccessMessageMixin,CreateView):
    model = Connexion
    form_class = ConnexionForm
    template_name = 'login_screen.html'
    success_url = reverse_lazy('connexion')
    success_message = 'Connexion Successfully'
    
    def login_view(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            # Vérifiez si l'utilisateur existe dans la table Etudiant
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                # Enregistrez une entrée dans la table Connexion
                Connexion.objects.create(email=email)
                
                # Connectez l'utilisateur et redirigez-le vers la page d'accueil
                login(request, user)
                return redirect('index')
            else:
                # Si l'authentification échoue, affichez un message d'erreur
                error_message = "L'adresse e-mail ou le mot de passe est incorrect."
                return render(request, 'login_screen.html', {'error_message': error_message})
        else:
            return render(request, 'login_screen.html')


# def login_view(request):
#     if request.method == 'POST':
#         form = ConnexionForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 form.add_error(None, 'Email ou mot de passe invalide')
#     else:
#         form = ConnexionForm()
#     return render(request, 'login_screen.html', {'form': form})
    
    
    
    
