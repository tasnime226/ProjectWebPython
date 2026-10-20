from django.test import TestCase
from django.utils import timezone

from .models import Entreprise, utilisateur


class UtilisateurIdGenerationTests(TestCase):
    def test_generate_user_id_uses_highest_existing_id(self):
        year_prefix = f"{timezone.now():%Y}_user_"
        utilisateur.objects.create(
            user_id=f"{year_prefix}00",
            username="premier",
            email="premier@gmail.com",
            password="!",
        )
        utilisateur.objects.create(
            user_id=f"{year_prefix}01",
            username="deuxieme",
            email="deuxieme@gmail.com",
            password="!",
        )

        self.assertEqual(
            utilisateur._generate_user_id(),
            f"{year_prefix}02",
        )

    def test_entreprise_can_be_saved_with_a_gerant(self):
        gerant = utilisateur.objects.create(
            username="gerant",
            email="gerant@gmail.com",
            password="!",
        )

        entreprise = Entreprise.objects.create(
            raison_sociale="Entreprise de test",
            matricule_fiscale="1234567AAM000",
            adresse="Adresse de test suffisamment longue",
            gerant=gerant,
        )

        self.assertIsNotNone(entreprise.pk)
