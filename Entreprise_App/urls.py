from django.urls import path

from .views import (
    EntrepriseCreateView,
    EntrepriseDeleteView,
    EntrepriseListView,
    EntrepriseUpdateView,
)

urlpatterns = [
    path('', EntrepriseListView.as_view(), name='entreprise_list'),
    path('ajouter/', EntrepriseCreateView.as_view(), name='entreprise_create'),
    path('<int:pk>/modifier/', EntrepriseUpdateView.as_view(), name='entreprise_update'),
    path('<int:pk>/supprimer/', EntrepriseDeleteView.as_view(), name='entreprise_delete'),
]
