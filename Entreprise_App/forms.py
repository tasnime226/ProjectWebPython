
from django import forms
from .models import Entreprise,utilisateur
from django.contrib.auth.forms import UserCreationForm



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


class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = utilisateur
        #fields =('username', 'email', 'telephone','role')
        fields =UserCreationForm.Meta.fields + ('email', 'telephone','role')  # Ajoutez les champs supplémentaires ici