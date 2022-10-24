from django.test import TestCase
from django.urls import reverse


class HomepageViews(TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'openrider/home.html')


class LegalsViews(TestCase):

    def test_legals(self):
        response = self.client.get(reverse('legals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'openrider/legals.html')
