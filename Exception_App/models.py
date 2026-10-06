from django.db import models
from Entreprise_App.models import Entreprise
from django.core.exceptions import ValidationError

# Create your models here.


class Exception(models.Model):
    reference = models.CharField(max_length=20,unique=True)
    ville_depart= models.CharField( max_length=100)
    ville_arrivee = models.CharField(
        max_length=100
    )
    poids_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
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
 