from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class Test_Register_Views(TestCase):

    def test_register_page(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_account_valid(self):
        response = self.client.post("/users/register/",
                                    {
                                        "username": "MisterMe59",
                                        "email": 'misterme59@test.fr',
                                        "password1": "motdepassemega59",
                                        "password2": "motdepassemega59"
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'openrider/home.html')

    def test_register_account_invalid(self):
        response = self.client.post("/users/register/",
                                    {
                                        "username": "MisterMe59",

                                        "password1": "motdepassemega59",
                                        "password2": "motdepassemega59"
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


class Test_Login_View(TestCase):

    def SetUp(self):
        self.data = {'username': 'papa',
                     'email': 'papa@gmail.com',
                     'password1': 'papaoutes13',
                     'password2': 'papaoutes13'}
        User.objects.create_user(self.data)

    def test_login(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_valid(self):
        response = self.client.post("/users/login/", {
                                            'username': 'papa',
                                            'password': 'kevin1234'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class Test_Logout_View(TestCase):

    def SetUp(self):
        User.objects.create_user(
            username="UserTest",
            email="usertest@test.fr",
            password="megamotdepasse59"
            )

    def test_logout(self):
        self.client.login(username="UserTest", password="megamotdepasse59")
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')


class ProfileViews(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="UserTest",
            email="usertest@test.fr",
            password="megamotdepasse59"
            )

    def test_account_when_logged_in(self):
        self.client.login(username="UserTest", password="megamotdepasse59")
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')


class FavViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_fav_when_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:fav'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/fav.html')

    def test_fav_when_logged_out(self):
        response = self.client.get(reverse('users:fav'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/login/?next=/users/fav/')


class DeleteAccountView(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_delete_account(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(
                            reverse('users:delete_account'),
                            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'openrider/home.html')


class ContactView(TestCase):

    def test_delete_account(self):
        response = self.client.get(reverse('users:contact'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
