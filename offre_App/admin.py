from django.contrib import admin
from .models import Offre


class OffreAdmin(admin.ModelAdmin):
    list_display = (
        'prix',
        'delai_jours',
        'statut',
        'expedition',
        'transporteur',
        'vehicule',
        'date_proposition',
    )

    list_filter = ('statut', 'date_proposition')

    list_editable = ('statut',)

    search_fields = (
        'expedition__reference',
        'transporteur__raison_sociale',
        'vehicule__immatriculation',
    )

    ordering = ('-date_proposition',)

    list_per_page = 5

    readonly_fields = ('date_proposition', 'created_at', 'updated_at')

    fieldsets = (
        (
            'Informations de l\'offre',
            {
                'fields': (
                    'prix',
                    'delai_jours',
                    'statut',
                ),
                'description': (
                    "Renseignez le prix proposé (en devise), le délai de livraison "
                    "en jours et le statut de l'offre."
                ),
            },
        ),
        (
            'Relations',
            {
                'fields': (
                    'expedition',
                    'transporteur',
                    'vehicule',
                ),
                'description': (
                    "Sélectionnez l'expédition concernée, le transporteur "
                    "qui propose l'offre et le véhicule affecté. "
                    "Le véhicule doit appartenir au transporteur et être disponible."
                ),
            },
        ),
        (
            'Métadonnées',
            {
                'fields': (
                    'date_proposition',
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',),
                'description': "Informations système générées automatiquement.",
            },
        ),
    )


# Register your models here.
admin.site.register(Offre, OffreAdmin)