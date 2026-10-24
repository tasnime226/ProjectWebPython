from django.urls import path

from .views import (
    VehiculeCreateView,
    VehiculeDeleteView,
    VehiculeListView,
    VehiculeUpdateView,
)

urlpatterns = [
    path('', VehiculeListView.as_view(), name='vehicule_list'),
    path('ajouter/', VehiculeCreateView.as_view(), name='vehicule_create'),
    path('<int:pk>/modifier/', VehiculeUpdateView.as_view(), name='vehicule_update'),
    path('<int:pk>/supprimer/', VehiculeDeleteView.as_view(), name='vehicule_delete'),
]
