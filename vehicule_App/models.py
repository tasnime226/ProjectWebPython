from django.db import models
from Entreprise_App.models import Entreprise

# Create your models here.

class Vehicule(models.Model):

    immatriculation = models.CharField(
        max_length=11,
        unique=True
    )

    type_vehicule = models.CharField(
        max_length=20,
        choices=[
            ('camionnette', 'Camionnette'),
            ('fourgon', 'Fourgon'),
            ('camion porteur', 'Camion porteur'),
            ('porteur', 'Porteur')
        ]
    )

    capacite_kg = models.PositiveIntegerField()

    disponible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    proprietaire = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name='vehicules'
    )