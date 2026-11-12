from django.urls import path
from .views import *

app_name = "vehicule"

urlpatterns = [

    # Vues fonctionnelles
    path('list/', listVehicules, name='list'),
    path('details/<int:pk>/', detailsVehicule, name='details'),
    path('supprimer/<int:pk>/', supprimerVehicule, name='supprimer'),

    # Vues génériques
    path('vehicule_list/', Vehicule_list.as_view(), name='vehicule_list'),

    path(
        'vehicule_details/<int:pk>/',
        Vehicule_details.as_view(),
        name='vehicule_details_class'
    ),

    path(
        'vehicule_delete/<int:pk>/',
        Vehicule_delete.as_view(),
        name='vehicule_delete_class'
    ),

    path(
        'vehicule_create/',
        Vehicule_create.as_view(),
        name='vehicule_create_class'
    ),

    path(
        'vehicule_update/<int:pk>/',
        Vehicule_update.as_view(),
        name='vehicule_update_class'
    ),
]