from django.shortcuts import render, redirect, get_object_or_404 # <-- Importez redirect et get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Exception
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ExceptionForm
from django.views.generic import UpdateView



def home(request):
    return HttpResponse("<h1>welcome to ...</h1>")

def welcome(request,name):
    return HttpResponse(f"Hello { name }")

def listExpeditions(request):
    list =Exception.objects.all()
    return render(request,'expedition/list.html',{"liste":list})

def detailsExpedition(request, pk):
    expedition = Exception.objects.get(pk=pk)
    return render(request, 'expedition/details.html', {'exp': expedition})

@require_POST
def supprimerExpedition(request, pk):
    # Récupère l'objet ou renvoie une erreur 404 s'il n'existe pas
    expedition = get_object_or_404(Exception, pk=pk)
    expedition.delete()
    return redirect('expedition:list')


class Exception_list(ListView):
    model = Exception
    template_name = 'expedition/list.html'
    context_object_name = 'liste'


class Exception_details(DetailView):
    model = Exception
    template_name = 'expedition/details.html'
    context_object_name = 'exp'


class Expedition_delete(DeleteView):
    model = Exception
    template_name = 'expedition/confirm_delete.html'
    success_url = reverse_lazy('expedition:list')


class Expedition_create(CreateView):
    model = Exception
    #fields = '__all__'
    template_name = 'expedition/form.html'
    success_url = reverse_lazy('expedition:list')
    form_class = ExceptionForm  # Utilisez le formulaire personnalisé pour inclure le widget de date


class Expedition_update(UpdateView):
    model = Exception
    template_name = 'expedition/form.html'
    success_url = reverse_lazy('expedition:list')
    form_class = ExceptionForm  # Utilisez le formulaire personnalisé pour inclure le widget de date
    
    
    