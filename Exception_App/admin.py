from django.contrib import admin
from .models import Exception


class ExceptionAdmin(admin.ModelAdmin):
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