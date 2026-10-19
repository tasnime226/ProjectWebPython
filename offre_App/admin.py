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


# Register your models here.
admin.site.register(Offre, OffreAdmin)