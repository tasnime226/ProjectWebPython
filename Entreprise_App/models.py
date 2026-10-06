from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Create your models here.

def validate_email(value):
    if not value:
        raise ValidationError("L'adresse e-mail est obligatoire.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("Format invalide")

    


class utilisateur(AbstractUser):
    user_id =models.CharField(max_length=8,primary_key=True)
    email = models.EmailField(unique=True, validators=[validate_email])
    role = models.CharField(max_length=20,choices=[('admin','Admin'),('chargeur','chargeur'),('transporteur','Transporteur')],default='chargeur')
    telephone = models.CharField(max_length=15,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


matricule_fiscale_validator = RegexValidator(
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Format incorrect - ex. 1234567AAM000 ou 1234567-A-A-M-000"
)


class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200,null=False,blank=False)
    matricule_fiscale = models.CharField(max_length=17 ,unique=True, validators=[matricule_fiscale_validator])
    Type_entrprise = models.CharField(max_length=100,choices=[('chargeur','Chargeur'),('transporteur','Transporteur')],default='chargeur')
    adresse = models.TextField(
    validators=[
        MinLengthValidator(20, "L'adresse doit contenir au moins 20 caractères"),
        MaxLengthValidator(300, "L'adresse doit contenir au plus 300 caractères")
    ]
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant =models.OneToOneField(utilisateur,on_delete=models.CASCADE,related_name='entreprise')


def save(self, *args, **kwargs):

    if not self.user_id:
        self.user_id= self._generate_user_id()

    self.full_clean()

    super().save(*args, **kwargs)

