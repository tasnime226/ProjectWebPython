from django.urls import path

from .views import (
    ExpeditionCreateView,
    ExpeditionDeleteView,
    ExpeditionListView,
    ExpeditionUpdateView,
)

urlpatterns = [
    path('', ExpeditionListView.as_view(), name='expedition_list'),
    path('ajouter/', ExpeditionCreateView.as_view(), name='expedition_create'),
    path('<int:pk>/modifier/', ExpeditionUpdateView.as_view(), name='expedition_update'),
    path('<int:pk>/supprimer/', ExpeditionDeleteView.as_view(), name='expedition_delete'),
]
