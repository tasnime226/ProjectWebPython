from django.test import TestCase
from django.urls import reverse


class ApplicationPageTests(TestCase):
    def test_dashboard_and_module_lists_render(self):
        page_names = (
            'dashboard',
            'vehicule_list',
            'offre_list',
            'entreprise_list',
            'expedition_list',
        )

        for page_name in page_names:
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))
                self.assertEqual(response.status_code, 200)

    def test_module_creation_forms_render(self):
        page_names = (
            'vehicule_create',
            'offre_create',
            'entreprise_create',
            'expedition_create',
        )

        for page_name in page_names:
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))
                self.assertEqual(response.status_code, 200)
