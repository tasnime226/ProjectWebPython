from django.contrib import admin
from .models import Vehicule


class VehiculeAdmin(admin.ModelAdmin):
    list_display = (
        'immatriculation',
        'type_vehicule',
        'capacite_kg',
        'disponible',
        'proprietaire',
    )

    list_filter = ('type_vehicule', 'disponible', 'proprietaire')

    ordering = ('immatriculation',)

    list_per_page = 5

    readonly_fields = ('created_at', 'updated_at')

    search_fields = ('immatriculation',)


# Register your models here.
admin.site.register(Vehicule, VehiculeAdmin)

