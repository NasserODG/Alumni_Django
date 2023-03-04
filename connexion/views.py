from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from connexion.form import ConnexionForm
from connexion.models import Connexion


def index(request):
    return render(request, 'base.html')

class connexion(SuccessMessageMixin,CreateView):
    model = Connexion
    form_class = ConnexionForm
    template_name = 'login_screen.html'
    success_url = reverse_lazy('connexion')
    success_message = 'Connexion Successfully'
