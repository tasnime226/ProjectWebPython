from django.db import models
from Entreprise_App.models import Entreprise
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

class Exception(models.Model):
    
    reference = models.CharField(max_length=20, unique=True, blank=True) 
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
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
    
    entreprise = models.ForeignKey('Entreprise_App.Entreprise', on_delete=models.CASCADE, related_name='exceptions', null=True)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.Type_entrprise != 'chargeur':
            raise ValidationError({'entreprise': "Une expedition ne peut etre creee que par une entreprise de type chargeur"})  

    @classmethod
    def _generate_reference(cls): # cls et non classs
        annee = timezone.now().strftime("%Y")
        prefix = f"EXP_{annee}_"

      
        dernier = cls.objects.filter(reference__startswith=prefix).order_by('-reference').first()
        
      
        compteur = (int(dernier.reference[-5:]) + 1 if dernier else 1)
        
        if compteur > 99999:
            raise ValidationError('Limit exceeded') 
            
        return f'{prefix}{compteur:05d}'

    def save(self, *args, **kwargs):
       
        if not self.reference:
            self.reference = self._generate_reference()
        
        self.full_clean() 
        super().save(*args, **kwargs) 