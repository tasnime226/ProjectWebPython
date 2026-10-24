from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Entreprise


class EntrepriseListView(ListView):
    model = Entreprise
    template_name = 'shared/list.html'
    context_object_name = 'objects'
    ordering = ('raison_sociale',)
    columns = (
        ('raison_sociale', 'Raison sociale'),
        ('matricule_fiscale', 'Matricule fiscale'),
        ('Type_entrprise', 'Type'),
        ('gerant', 'Gérant'),
        ('adresse', 'Adresse'),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Entreprises'
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
        context['create_url'] = 'entreprise_create'
        context['update_url'] = 'entreprise_update'
        context['delete_url'] = 'entreprise_delete'
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


class EntrepriseCreateView(CreateView):
    model = Entreprise
    fields = (
        'raison_sociale',
        'matricule_fiscale',
        'Type_entrprise',
        'adresse',
        'gerant',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('entreprise_list')
    extra_context = {'title': 'Ajouter une entreprise', 'cancel_url': 'entreprise_list'}


class EntrepriseUpdateView(UpdateView):
    model = Entreprise
    fields = (
        'raison_sociale',
        'matricule_fiscale',
        'Type_entrprise',
        'adresse',
        'gerant',
    )
    template_name = 'shared/form.html'
    success_url = reverse_lazy('entreprise_list')
    extra_context = {'title': 'Modifier une entreprise', 'cancel_url': 'entreprise_list'}


class EntrepriseDeleteView(DeleteView):
    model = Entreprise
    template_name = 'shared/confirm_delete.html'
    success_url = reverse_lazy('entreprise_list')
    extra_context = {'title': 'Supprimer une entreprise', 'cancel_url': 'entreprise_list'}
