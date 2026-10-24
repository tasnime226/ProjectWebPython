from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Offre


class OffreListView(ListView):
    model = Offre
    template_name = 'shared/list.html'
    context_object_name = 'objects'
    ordering = ('-date_proposition',)
    columns = (
        ('expedition', 'Expédition'),
        ('transporteur', 'Transporteur'),
        ('vehicule', 'Véhicule'),
        ('prix', 'Prix'),
        ('delai_jours', 'Délai (jours)'),
        ('statut', 'Statut'),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Offres'
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
        context['create_url'] = 'offre_create'
        context['update_url'] = 'offre_update'
        context['delete_url'] = 'offre_delete'
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


class OffreCreateView(CreateView):
    model = Offre
    fields = (
        'prix',
        'delai_jours',
        'statut',
        'expedition',
        'transporteur',
        'vehicule',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('offre_list')
    extra_context = {'title': 'Ajouter une offre', 'cancel_url': 'offre_list'}


class OffreUpdateView(UpdateView):
    model = Offre
    fields = (
        'prix',
        'delai_jours',
        'statut',
        'expedition',
        'transporteur',
        'vehicule',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('offre_list')
    extra_context = {'title': 'Modifier une offre', 'cancel_url': 'offre_list'}


class OffreDeleteView(DeleteView):
    model = Offre
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('offre_list')
    extra_context = {'title': 'Supprimer une offre', 'cancel_url': 'offre_list'}
