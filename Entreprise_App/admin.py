
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Entreprise, utilisateur 
from vehicule_App.models import Vehicule

# Configuration de l'administration
admin.site.site_header = "Trasconnect - Administration"
admin.site.site_title = "Trasconnect"
admin.site.index_title = "Tableau de bord de l'administration"


@admin.register(utilisateur)
class UtilisateurAdmin(UserAdmin):

    list_display = (
        'user_id',
        'username',
        'email',
        'role',
        'telephone',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_filter = ('role', 'is_active', 'created_at')

    search_fields = ('user_id', 'username', 'email', 'telephone')

    ordering = ('username',)

    list_per_page = 10

    readonly_fields = (
        'user_id',
        'date_joined',
        'last_login',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Identité', {
            'fields': (
                'user_id',
                'username',
                'email',
                'telephone',
                'role',
            )
        }),
        ('Rôles et permissions', {
            'fields': (
                'password',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Dates', {
            'fields': (
                'date_joined',
                'last_login',
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',),
        }),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'telephone',
                'role',
                'password1',
                'password2',
            ),
        }),
    )

class VehiculeInline(admin.TabularInline):
    model = Vehicule
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible')
    extra = 1
    show_change_link = True


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    inlines = [VehiculeInline]

    list_display = (
        'raison_sociale',
        'matricule_fiscale',
        'adresse',
        'Type_entrprise',
        'gerant',
    )

    list_filter = ('Type_entrprise',)

    search_fields = (
        'raison_sociale',
        'matricule_fiscale',
        'gerant__username',
        'gerant__email',
    )

    ordering = ('raison_sociale',)

    list_per_page = 5

    readonly_fields = ('created_at', 'updated_at')
