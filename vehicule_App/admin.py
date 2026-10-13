from django.contrib import admin
from .models import Vehicule

class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('disponible', 'capacite_kg ', 'type_vehicule', 'immatriculation')
    list_filter = ('type_vehicule', 'entreprise')
# Register your models here.
admin.site.register(Vehicule)
