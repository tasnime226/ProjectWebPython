from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Vehicule
from .forms import VehiculeForm

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# 1. LIST : afficher tous les véhicules

def listVehicules(request):
    liste = Vehicule.objects.all()
    return render(request, 'vehicule/list.html', {'liste': liste})


# 2. DETAILS : afficher un véhicule

def detailsVehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    return render(request, 'vehicule/details.html', {'veh': vehicule})


# 3. DELETE : supprimer un véhicule

@require_POST
def supprimerVehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    vehicule.delete()
    return redirect('vehicule:list')


# 4. LIST avec ListView

class Vehicule_list(ListView):
    model = Vehicule
    template_name = 'vehicule/list.html'
    context_object_name = 'liste'


# 5. DETAILS avec DetailView

class Vehicule_details(DetailView):
    model = Vehicule
    template_name = 'vehicule/details.html'
    context_object_name = 'veh'


# 6. DELETE avec DeleteView

class Vehicule_delete(DeleteView):
    model = Vehicule
    template_name = 'vehicule/confirm_delete.html'
    success_url = reverse_lazy('vehicule:list')


# 7. CREATE avec CreateView

class Vehicule_create(CreateView):
    model = Vehicule
    template_name = 'vehicule/form.html'
    form_class = VehiculeForm
    success_url = reverse_lazy('vehicule:list')


# 8. UPDATE avec UpdateView

class Vehicule_update(UpdateView):
    model = Vehicule
    template_name = 'vehicule/form.html'
    form_class = VehiculeForm
    success_url = reverse_lazy('vehicule:list')