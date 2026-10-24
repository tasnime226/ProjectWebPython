from django.shortcuts import render

from Entreprise_App.models import Entreprise
from Exception_App.models import Exception
from offre_App.models import Offre
from vehicule_App.models import Vehicule


def dashboard(request):
    context = {
        'vehicule_count': Vehicule.objects.count(),
        'offre_count': Offre.objects.count(),
        'entreprise_count': Entreprise.objects.count(),
        'expedition_count': Exception.objects.count(),
    }
    return render(request, 'dashboard.html', context)
