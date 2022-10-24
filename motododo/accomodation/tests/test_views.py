from django.test import TestCase
from django.urls import reverse
from accomodation.models import Category,\
                                Parking,\
                                AddAccomodation,\
                                Accomodation,\
                                Comment
from django.contrib.auth.models import User


class Accomodation_Views_Test(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

        self.admin_username = "moi"
        self.admin_email = "moi@moi.fr"
        self.admin_password = "passadmin"
        self.admin = User.objects.create_superuser(
                self.admin_username,
                self.admin_email,
                self.admin_password,
        )

        category = Category.objects.create(name="gite")
        parking = Parking.objects.create(parking='clos')

        addAccomodation_statut_list = (
            ("Non_lu", "Non lu"),
            ("Archive", "Archivé"),
        )
        accomodation_waiting = AddAccomodation.objects.create(
            addAccomodation_name="Paulo",
            addAccomodation_category=category,
            addAccomodation_road="rue du polo",
            addAccomodation_zipcode="56400",
            addAccomodation_city="Auray",
            addAccomodation_phone="0623451278",
            addAccomodation_email="paulo@test.fr",
            addAccomodation_parking=parking,
            addAccomodation_description="Très bien!",
            addAccomodation_statut=addAccomodation_statut_list[0][0]
        )
        self.accomodation_waiting = accomodation_waiting

        accomodation_checked = AddAccomodation.objects.create(
            addAccomodation_name="Maison",
            addAccomodation_category=category,
            addAccomodation_road="rue Jean Jaures",
            addAccomodation_zipcode="56400",
            addAccomodation_city="Auray",
            addAccomodation_phone="0234567890",
            addAccomodation_email="maisono@test.fr",
            addAccomodation_parking=parking,
            addAccomodation_description="Cool!",
            addAccomodation_statut=addAccomodation_statut_list[1][0]
        )
        self.accomdation_checked = accomodation_checked

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
        accomodation2 = Accomodation.objects.create(
            name="Kyriad",
            category=category,
            road="rue de la rivière",
            zipcode="56400",
            city="Auray",
            phone="0653438712",
            email="test2@test.fr",
            park=parking,
            description="Très bien!",
            lat='42.141516',
            lon='2.363738',
        )
        self.accomodation2 = accomodation2
        self.final_result = [self.accomodation, self.accomodation2]

    def test_add_view_notlogged(self):
        response = self.client.get(reverse('accomodation:add'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/accomodation/add/')

    def test_add_view_logged(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('accomodation:add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accomodation/add.html')

    def test_search_view_isempty(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/accomodation/search/?search=%s' % (''))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accomodation/all_result.html')

    def test_search_view_noresult(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(
            '/accomodation/search/?search=%s' % ('Paris')
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accomodation/noresult.html')

    def test_details_view(self):
        self.client.login(username=self.username, password=self.password)
        test = Accomodation.objects.get(name="Treulan")
        comments = Comment.objects.filter(accomodation=test)
        response = self.client.get(
            '/accomodation/details/%d' % (test.auto_increment_id)
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accomodation/details.html')
        self.assertEqual((response.context['accomodation']), test)
        self.assertQuerysetEqual((response.context['comments']), comments)
        self.assertEqual((response.context['total_likes']), test.total_likes())

    def test_like_view(self):
        user_id = self.user.id
        self.accomodation.likes.add(user_id)
        response = self.client.get(reverse('accomodation:like'), follow=True)
        self.assertTrue(self.accomodation.likes.filter(id=user_id).exists())
        self.assertFalse(self.accomodation2.likes.filter(id=user_id).exists())
        self.assertEqual(response.status_code, 200)

    def test_validation_waiting_view(self):
        self.client.login(
            username=self.admin_username,
            password=self.admin_password
            )
        waiting = AddAccomodation.objects.filter(
            addAccomodation_statut="Non_lu"
            )
        response = self.client.get(
            reverse('accomodation:validation_waiting')
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'accomodation/validation_waiting.html'
            )
        self.assertQuerysetEqual(
            (response.context['validation_waiting']),
            (repr(elt) for elt in waiting))

    def test_validation_checked_view(self):
        self.client.login(
            username=self.admin_username,
            password=self.admin_password
            )
        checked = AddAccomodation.objects.get(
            addAccomodation_name="Maison"
            )
        checked.lat = "12.123456"
        checked.lon = "42.123456"
        checked.save()
        verify = Accomodation.objects.filter(
            lat=checked.lat).filter(
                lon=checked.lon)
        verify2 = Accomodation.objects.filter(
            lat=self.accomodation.lat).filter(
                lon=self.accomodation.lon)
        self.assertFalse(verify)
        self.assertTrue(verify2)
        response = self.client.get(
            reverse('accomodation:validation_checked'),
            follow=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'accomodation/validation_waiting.html'
            )
