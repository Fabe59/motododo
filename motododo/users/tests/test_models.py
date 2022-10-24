from django.test import TestCase
from accomodation.models import Category, Parking, Accomodation
from users.models import Favorite
from django.contrib.auth.models import User


class ModelsTest(TestCase):

    def test_Favorite_model(self):
        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')
        user = User.objects.create_user(
            username="UtilisateurTest",
            first_name="utilisateur",
            last_name="Test",
            password="Azertyui4552"
        )
        accomodation = Accomodation.objects.create(
            name="Treulan",
            category=category,
            road="rue du pont",
            zipcode="56400",
            city="Auray",
            phone="0652535455",
            email="test@test.fr",
            park=parking,
            description="Très bien!",
            lat='42.121314',
            lon='2.353637',
        )
        Favorite.objects.create(user=user, accomodation_saved=accomodation)
        favorite = Favorite.objects.all().first()
        self.assertEqual(favorite.user, user)
        self.assertEqual(favorite.accomodation_saved, accomodation)
        self.assertEqual(
            str(favorite),
            "UtilisateurTest - Treulan, None rue du pont, 56400, Auray"
            " - 42.121314, 2.353637"
            )
