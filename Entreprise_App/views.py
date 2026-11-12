
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Entreprise
from .forms import EntrepriseForm


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
