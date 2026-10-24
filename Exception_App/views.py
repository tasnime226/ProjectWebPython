from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Exception


class ExpeditionListView(ListView):
    model = Exception
    template_name = 'shared/list.html'
    context_object_name = 'objects'
    ordering = ('-date_souhaitee',)
    columns = (
        ('reference', 'Référence'),
        ('ville_depart', 'Départ'),
        ('ville_arrivee', 'Arrivée'),
        ('poids_kg', 'Poids (kg)'),
        ('date_souhaitee', 'Date souhaitée'),
        ('statut', 'Statut'),
        ('entreprise', 'Entreprise'),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Expéditions'
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
        context['create_url'] = 'expedition_create'
        context['update_url'] = 'expedition_update'
        context['delete_url'] = 'expedition_delete'
        return context

    @staticmethod
    def _display_value(item, field):
        display_method = getattr(item, f'get_{field}_display', None)
        value = (
            display_method()
            if callable(display_method)
            else getattr(item, field)
        )
        return str(value) if value not in (None, '') else '—'


class ExpeditionCreateView(CreateView):
    model = Exception
    fields = (
        'ville_depart',
        'ville_arrivee',
        'poids_kg',
        'date_souhaitee',
        'description',
        'statut',
        'entreprise',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('expedition_list')
    extra_context = {'title': 'Ajouter une expédition', 'cancel_url': 'expedition_list'}


class ExpeditionUpdateView(UpdateView):
    model = Exception
    fields = (
        'ville_depart',
        'ville_arrivee',
        'poids_kg',
        'date_souhaitee',
        'description',
        'statut',
        'entreprise',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('expedition_list')
    extra_context = {'title': 'Modifier une expédition', 'cancel_url': 'expedition_list'}


class ExpeditionDeleteView(DeleteView):
    model = Exception
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('expedition_list')
    extra_context = {'title': 'Supprimer une expédition', 'cancel_url': 'expedition_list'}
