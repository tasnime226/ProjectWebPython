
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Entreprise
from .forms import EntrepriseForm,InscriptionForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProfilForm


class Entreprise_list(ListView):
    model = Entreprise
    template_name = 'entreprise/list.html'
    context_object_name = 'liste'


class Entreprise_details(DetailView):
    model = Entreprise
    template_name = 'entreprise/details.html'
    context_object_name = 'ent'


class Entreprise_create(CreateView):
    model = Entreprise
    template_name = 'entreprise/form.html'
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprise:entreprise_list')


class Entreprise_update(UpdateView):
    model = Entreprise
    template_name = 'entreprise/form.html'
    form_class = EntrepriseForm
    success_url = reverse_lazy('entreprise:entreprise_list')


class Entreprise_delete(DeleteView):
    model = Entreprise
    template_name = 'entreprise/confirm_delete.html'
    success_url = reverse_lazy('entreprise:entreprise_list')


def inscriptionView(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})



class ProfilView(LoginRequiredMixin, TemplateView):
    template_name = 'profil/profil.html'
    login_url = 'Login'


class ProfilUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfilForm
    template_name = 'profil/profil_form.html'
    success_url = reverse_lazy('entreprise:profil')

    def get_object(self):
        return self.request.user


class ProfilDelete(LoginRequiredMixin, DeleteView):
    template_name = 'profil/profil_confirm_delete.html'
    success_url = reverse_lazy('Login')

    def get_object(self):
        return self.request.user