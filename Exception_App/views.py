from django.shortcuts import render, redirect, get_object_or_404 # <-- Importez redirect et get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Exception



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