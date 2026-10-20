from django.contrib import admin
from .models import Exception


class EnRetardAdmin(admin.SimpleListFilter):
    titre = 'En retard'
    parameter_name = "en_retard"
    def lookups(self, request, model_admin):
        return (
            ('oui', 'Oui'),
            ('non', 'Non'),
        )
    def queryest(self,request,queryest):
        aujourd_hui = timezone.now().date()
        if self.value() == 'oui':
            return queryest.filter(statut="publiee",date_souhaitee__lt=aujourd_hui)
        if self.value() == 'non':
            return queryest.exclude(statut="publiee",date_souhaitee__lt=aujourd_hui)
        return queryest
    
@admin.action(description="Passer à : Publiée")
def marquer_publiee(modeladmin, request, queryset):
    queryset.update(statut='publiee')


@admin.action(description="Passer à : Attribuée")
def marquer_attribuee(modeladmin, request, queryset):
    queryset.update(statut='attribuee')


@admin.action(description="Passer à : En cours")
def marquer_en_cours(modeladmin, request, queryset):
    queryset.update(statut='en_cours')


@admin.action(description="Passer à : Livrée")
def marquer_livree(modeladmin, request, queryset):
    queryset.update(statut='livree')


@admin.action(description="Passer à : Annulée")
def marquer_annulee(modeladmin, request, queryset):
    queryset.update(statut='annulee')


class ExceptionAdmin(admin.ModelAdmin):
    actions = [
        marquer_publiee,
        marquer_attribuee,
        marquer_en_cours,
        marquer_livree,
        marquer_annulee,
    ]
    list_display = ('reference', 'date_souhaitee', 'statut')
    list_filter = ('created_at', 'entreprise')
    ordering = ('-date_souhaitee',)
    list_per_page = 5
    readonly_fields = ('reference', 'created_at', 'updated_at')
    search_fields = ('reference', 'statut')
    list_editable = ('statut',)

    fieldsets = (
        ('Information', {
            'fields': (
                'reference',
                'ville_depart',
                'ville_arrivee',
                'poids_kg',
                'date_souhaitee',
                'description',
                'statut',
                'entreprise',
            )
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


# Register your models here.
admin.site.register(Exception, ExceptionAdmin)