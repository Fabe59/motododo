from django.test import TestCase
from django.urls import reverse, resolve
from users.views import register,\
    profile,\
    fav,\
    delete_fav,\
    delete_account,\
    contact
from django.contrib.auth import views as auth_views


class Users_Url_Test(TestCase):

    def test_register_url(self):
        url = reverse('users:register')
        self.assertEqual(resolve(url).func, register)

    def test_profile_url(self):
        url = reverse('users:profile')
        self.assertEqual(resolve(url).func, profile)

    def test_login_url(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_fav_url(self):
        url = reverse('users:fav')
        self.assertEqual(resolve(url).func, fav)

    def test_delete_fav_url(self):
        url = reverse('users:delete_fav')
        self.assertEqual(resolve(url).func, delete_fav)

    def test_delete_account_url(self):
        url = reverse('users:delete_account')
        self.assertEqual(resolve(url).func, delete_account)

    def test_contact_url(self):
        url = reverse('users:contact')
        self.assertEqual(resolve(url).func, contact)
