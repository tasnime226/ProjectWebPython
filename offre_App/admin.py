from django.contrib import admin
from .models import Offre

class OffreAdmin(admin.ModelAdmin):
    list_display = ('prix', 'delai_jours', 'statut')
    list_filter = ('statut',)
    editable_fields = ('statut',)

# Register your models here.
admin.site.register(Offre)
