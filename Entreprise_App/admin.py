from django.contrib import admin
from .models import Entreprise, utilisateur


class EntrepriseAdmin(admin.ModelAdmin):
    list_display = (
        'raison_sociale',
        'matricule_fiscale',
        'adresse',
        'Type_entrprise',
        'gerant',
    )

    list_filter = ('Type_entrprise',)

    search_fields = ('raison_sociale', 'matricule_fiscale')

    ordering = ('raison_sociale',)

    list_per_page = 5

    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(utilisateur)