from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Vehicule


class VehiculeListView(ListView):
    model = Vehicule
    template_name = 'shared/list.html'
    context_object_name = 'objects'
    ordering = ('immatriculation',)
    title = 'Véhicules'
    columns = (
        ('immatriculation', 'Immatriculation'),
        ('type_vehicule', 'Type'),
        ('capacite_kg', 'Capacité (kg)'),
        ('disponible', 'Disponible'),
        ('proprietaire', 'Propriétaire'),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['columns'] = [label for _, label in self.columns]
        context['rows'] = [
            {
                'object': item,
                'values': [
                    self._display_value(item, field)
                    for field, _ in self.columns
                ],
            }
            for item in context['objects']
        ]
        context['create_url'] = 'vehicule_create'
        context['update_url'] = 'vehicule_update'
        context['delete_url'] = 'vehicule_delete'
        return context

    @staticmethod
    def _display_value(item, field):
        display_method = getattr(item, f'get_{field}_display', None)
        value = (
            display_method()
            if callable(display_method)
            else getattr(item, field)
        )
        if isinstance(value, bool):
            return 'Oui' if value else 'Non'
        return str(value) if value not in (None, '') else '—'


class VehiculeCreateView(CreateView):
    model = Vehicule
    fields = (
        'immatriculation',
        'type_vehicule',
        'capacite_kg',
        'disponible',
        'proprietaire',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('vehicule_list')
    extra_context = {'title': 'Ajouter un véhicule', 'cancel_url': 'vehicule_list'}


class VehiculeUpdateView(UpdateView):
    model = Vehicule
    fields = (
        'immatriculation',
        'type_vehicule',
        'capacite_kg',
        'disponible',
        'proprietaire',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('vehicule_list')
    extra_context = {'title': 'Modifier un véhicule', 'cancel_url': 'vehicule_list'}


class VehiculeDeleteView(DeleteView):
    model = Vehicule
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('vehicule_list')
    extra_context = {'title': 'Supprimer un véhicule', 'cancel_url': 'vehicule_list'}
