
from django import forms
from .models import Entreprise


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            'raison_sociale',
            'matricule_fiscale',
            'Type_entrprise',
            'adresse',
            'gerant',
        ]

        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }
