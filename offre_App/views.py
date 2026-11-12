from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Offre
from .forms import OffreForm

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# 1. LIST : afficher toutes les offres

def listOffres(request):
    liste = Offre.objects.all()
    return render(request, 'offre/list.html', {'liste': liste})


# 2. DETAILS : afficher une offre

def detailsOffre(request, pk):
    offre = get_object_or_404(Offre, pk=pk)
    return render(request, 'offre/details.html', {'off': offre})


# 3. DELETE : supprimer une offre

@require_POST
def supprimerOffre(request, pk):
    offre = get_object_or_404(Offre, pk=pk)
    offre.delete()
    return redirect('offre:list')


# 4. LIST avec ListView

class Offre_list(ListView):
    model = Offre
    template_name = 'offre/list.html'
    context_object_name = 'liste'


# 5. DETAILS avec DetailView

class Offre_details(DetailView):
    model = Offre
    template_name = 'offre/details.html'
    context_object_name = 'off'


# 6. DELETE avec DeleteView

class Offre_delete(DeleteView):
    model = Offre
    template_name = 'offre/confirm_delete.html'
    success_url = reverse_lazy('offre:list')


# 7. CREATE avec CreateView

class Offre_create(CreateView):
    model = Offre
    template_name = 'offre/form.html'
    form_class = OffreForm
    success_url = reverse_lazy('offre:list')


# 8. UPDATE avec UpdateView

class Offre_update(UpdateView):
    model = Offre
    template_name = 'offre/form.html'
    form_class = OffreForm
    success_url = reverse_lazy('offre:list')