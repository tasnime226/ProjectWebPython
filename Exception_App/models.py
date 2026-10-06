from sys import prefix

from django.db import models
from Entreprise_App.models import Entreprise
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.


class Exception(models.Model):
    reference = models.CharField(max_length=20,unique=True)
    ville_depart= models.CharField( max_length=100)
    ville_arrivee = models.CharField(
        max_length=100
    )
    poids_kg = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0.01)]
)
    date_souhaitee = models.DateField()
    description = models.TextField()
    statut = models.CharField(
        max_length=20,
        choices=[
            ('publiee', 'Publiée'),
            ('attribuee', 'Attribuée'),
            ('en_cours', 'En cours'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée')
        ],
        default='publiee'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey('Entreprise_App.Entreprise', on_delete=models.CASCADE, related_name='exceptions')

    def clean(self):
        supper().clean()
        #Regle(s) metier
        if self.entreprise_id and self.entreprise.Type_entrprise != 'chargeur':
            raise ValidationError({'entreprise': "une expedition ne peut etre creee que par une entreprise de type chargeur"})  
    @classmethod
    def _generate_reference(classs):
        annee = timezone.now().strftime("%Y") #extraire annee
        prefix = f"EXP_{annee}_"

        dernier =(classs.objects.filter(reference__startswith=prefix).order_by('reference').first())
        compteur =(int(dernier.refernce[-5:]) + 1 if dernier else 1)
        if compteur > 99999:
            raise validationError('limit exceeded')
        return f'{prefix}{compteur:05d}'

def save (self, *args, **kwargs):
    if not self.reference:
        self.refernce = self._generate_reference()
        self.full_clean()
    super().save(*args, **kwargs)