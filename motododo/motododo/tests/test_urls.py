from django.test import TestCase
from openrider.views import home
from django.urls import reverse, resolve


class OpenRider_Urls_Test(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
