from django.urls import path
from .views import *

app_name = "offre"

urlpatterns = [

    # Vues fonctionnelles
    path('list/', listOffres, name='list'),
    path('details/<int:pk>/', detailsOffre, name='details'),
    path('supprimer/<int:pk>/', supprimerOffre, name='supprimer'),

    # Vues génériques
    path('offre_list/', Offre_list.as_view(), name='offre_list'),

    path(
        'offre_details/<int:pk>/',
        Offre_details.as_view(),
        name='offre_details_class'
    ),

    path(
        'offre_delete/<int:pk>/',
        Offre_delete.as_view(),
        name='offre_delete_class'
    ),

    path(
        'offre_create/',
        Offre_create.as_view(),
        name='offre_create_class'
    ),

    path(
        'offre_update/<int:pk>/',
        Offre_update.as_view(),
        name='offre_update_class'
    ),
]