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
        if self.transporteur_id and self.transporteur.Type_entrprise != 'transporteur':
            raise ValidationError({'transporteur': "offre relative a un chargeur."})     
        #Regle 2   
        if self.vehicule_id and self.transporteur_id and self.vehicule.proprietaire_id != self.transporteur_id:
            raise ValidationError({'vehicule': "le vehicule doit appartenir au transporteur de offre."})
        # Règle 3 : l'expédition doit être publiée
        if self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError({
        'expedition': "L'expédition n'est pas publiée."})
        
        # Règle 4 : une seule offre proposée active par entreprise
        if self.transporteur_id and self.expedition_id:
            offre_existante = Offre.objects.filter(
                 transporteur_id=self.transporteur_id,
                 expedition_id=self.expedition_id,
                 statut='proposee'
                  ).exclude(pk=self.pk).exists()
            if self.statut == 'proposee' and offre_existante:
                raise ValidationError({
                    'transporteur': "Cette entreprise possède déjà une offre proposée pour cette expédition."
                })
        # Règle 6 : le véhicule doit être disponible
        if self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError({
                'vehicule': "Le véhicule n'est pas disponible."
            })
        # Règle 7 : compatibilité entre le type de véhicule et le poids de l'expédition
        if self.vehicule_id and self.expedition_id:
            poids = float(self.expedition.poids_kg)
            type_vehicule = self.vehicule.type_vehicule

            capacites = {
                'camionnette': 1500,
                'fourgon': 3500,
                'camion porteur': 19000,
                'porteur': 26000,
            }
            if type_vehicule not in capacites or poids > capacites[type_vehicule]:
                raise ValidationError({
                    'vehicule':"Le type de véhicule n'est pas compatible avec le poids de l'expédition." })
                  

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
        if self.statut == 'acceptee':
            self.expedition.statut = 'attribuee'
            self.expedition.save()
            Offre.objects.filter(
                expedition=self.expedition,
                statut='proposee'
            ).exclude(pk=self.pk).update(statut='retiree')

    def __str__(self):
        return f'{self.expedition} — {self.transporteur} ({self.prix})'
