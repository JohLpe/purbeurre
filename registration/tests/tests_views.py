from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse


class TestsRegistrationViews(TestCase):
    """Tests registration views.py"""

    def setUp(self):

        self.client = Client()

    def test_register_page(self):
        """Tests if the register page can be reached"""

        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Tests if the login page can be reached"""

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        """Tests if logging out redirects to the homepage"""

        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')

    def test_redirect_after_registering(self):
        """Tests that user is redirected to login page after registration"""

        response = self.client.post(reverse('register'),
                                    {"username": "Testuser",
                                     "first_name": "Martin",
                                     "last_name": "Paul",
                                     "email": "qqchose@mail.com",
                                     "password1": 'lfnedTTzpv244fjf',
                                     "password2": 'lfnedTTzpv244fjf'})
        self.assertRedirects(response, '/registration/login/')

    def test_redirect_after_login(self):
        """Tests that user is redirected to homepage page after logging in"""

        self.user = User.objects.create_user('Testuser',
                                             'myemail@test.com',
                                             'lfnedTTzpv244fjf')
        response = self.client.post(reverse('login'),
                                    {"username": "Testuser",
                                     "password": 'lfnedTTzpv244fjf'})
        self.assertRedirects(response, '/')
