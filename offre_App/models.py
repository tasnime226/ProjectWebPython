from django.db import models
from Exception_App.models import Exception
from Entreprise_App.models import Entreprise
from vehicule_App.models import Vehicule    
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator



class Offre(models.Model):

    STATUT_CHOICES = [
        ('proposee', 'Proposée'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
        ('retiree', 'Retirée'),
    ]

    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    delai_jours = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='proposee'
    )

    date_proposition = models.DateField(auto_now_add=True)

    expedition = models.ForeignKey(
        Exception,
        on_delete=models.CASCADE
    )

    transporteur = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )

    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        # Règle métier 
        if self.transporteur and self.transporteur.Type_entrprise != 'transporteur':
            raise ValidationError({'transporteur': "offre relative a un chargeur."})     
        #Regle 2   
        if self.vehicule_id and self.transporteur_id and self.vehicule.entreprise_id != self.transporteur_id:
            raise ValidationError({'vehicule': "le vehicule doit appartenir au transporteur de offre."})

