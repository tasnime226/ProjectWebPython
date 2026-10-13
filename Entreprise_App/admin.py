from django.contrib import admin
from .models import Entreprise
from .models import utilisateur

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'adresse',  'Type_entrprise', 'gerant')
    list_filter = ('Type_entrprise',)
   
# Register your models here.
admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(utilisateur)
