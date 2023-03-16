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


def Connexion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['mot_de_passe']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Le nom d'utilisateur ou le mot de passe est incorrect"
            return render(request, 'login_screen.html', {'error_message': error_message})
    else:
        return render(request, 'login_screen.html')
    