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

    fieldsets = (
        (
            'Identification du véhicule',
            {
                'fields': (
                    'immatriculation',
                    'type_vehicule',
                ),
                'description': (
                    "L'immatriculation doit être unique. "
                    "Le type de véhicule détermine la capacité maximale "
                    "acceptée pour les offres (voir règles métier des offres)."
                ),
            },
        ),
        (
            'Caractéristiques et disponibilité',
            {
                'fields': (
                    'capacite_kg',
                    'disponible',
                ),
                'description': (
                    "La capacité doit être supérieure à 100 kg. "
                    "Un véhicule non disponible ne peut pas être affecté à une offre."
                ),
            },
        ),
        (
            'Propriétaire',
            {
                'fields': ('proprietaire',),
                'description': (
                    "Le véhicule doit appartenir à une entreprise de type "
                    "'transporteur' pour pouvoir être utilisé dans une offre."
                ),
            },
        ),
        (
            'Métadonnées',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',),
                'description': "Informations système générées automatiquement.",
            },
        ),
    )


# Register your models here.
admin.site.register(Vehicule, VehiculeAdmin)