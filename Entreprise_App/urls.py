
from django.urls import path
from .views import *
from .views import ProfilView, ProfilUpdate, ProfilDelete

app_name = "entreprise"

urlpatterns = [

    path(
        'entreprise_list/',
        Entreprise_list.as_view(),
        name='entreprise_list'
    ),

    path(
        'entreprise_details/<int:pk>/',
        Entreprise_details.as_view(),
        name='entreprise_details_class'
    ),

    path(
        'entreprise_create/',
        Entreprise_create.as_view(),
        name='entreprise_create_class'
    ),

    path(
        'entreprise_update/<int:pk>/',
        Entreprise_update.as_view(),
        name='entreprise_update_class'
    ),

    path(
        'entreprise_delete/<int:pk>/',
        Entreprise_delete.as_view(),
        name='entreprise_delete_class'
    ),
    path('profil/', ProfilView.as_view(), name='profil'),
    path('profil/modifier/', ProfilUpdate.as_view(), name='profil_modifier'),
    path('profil/supprimer/', ProfilDelete.as_view(), name='profil_supprimer'),
    
]
