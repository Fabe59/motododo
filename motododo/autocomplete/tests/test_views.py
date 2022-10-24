from django.test import TestCase
from django.urls import reverse
import json
from accomodation.models import Category, Parking, Accomodation


class Autocomplete(TestCase):

    def setUp(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        accomodation = Accomodation.objects.create(
            name="Treulan",
            category=category,
            road="rue du pont",
            zipcode="56400",
            city="Pluneret",
            phone="0652535455",
            email="test@test.fr",
            park=parking,
            description="Très bien!",
            lat='42.121314',
            lon='2.353637',
        )
        self.accomodation = accomodation

    def test_complete_views(self):
        response = self.client.get(reverse("autocomplete:complete"), {
            "term": "plu"
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(["Pluneret"]))
