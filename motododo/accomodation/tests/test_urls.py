from django.test import TestCase
from accomodation.views import add,\
                                search,\
                                details,\
                                like,\
                                validation_waiting,\
                                validation_checked,\
                                validation_refused,\
                                geoloc
from django.urls import reverse, resolve


class Accomodation_Urls_Test(TestCase):

    def test_add_url_resolves(self):
        url = reverse('accomodation:add')
        self.assertEquals(resolve(url).func, add)

    def test_search_url_resolves(self):
        url = reverse('accomodation:search')
        self.assertEquals(resolve(url).func, search)

    def test_geoloc_url_resolves(self):
        url = reverse('accomodation:geoloc')
        self.assertEquals(resolve(url).func, geoloc)

    def test_details_url_like(self):
        url = reverse('accomodation:details', args=['7'])
        self.assertEquals(resolve(url).func, details)

    def test_like_url_resolves(self):
        url = reverse('accomodation:like')
        self.assertEquals(resolve(url).func, like)

    def test_validation_waiting_url_resolves(self):
        url = reverse('accomodation:validation_waiting')
        self.assertEquals(resolve(url).func, validation_waiting)

    def test_validation_checked_url_resolves(self):
        url = reverse('accomodation:validation_checked')
        self.assertEquals(resolve(url).func, validation_checked)

    def test_validation_refused_url_resolves(self):
        url = reverse('accomodation:validation_refused')
        self.assertEquals(resolve(url).func, validation_refused)
