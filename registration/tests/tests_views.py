from django.test import TestCase, Client
from django.urls import reverse
from ..utils import NewUserForm


class TestsRegistrationViews(TestCase):
    """Tests registration views.py"""

    def setUp(self):

        self.client = Client()
        self.form = NewUserForm(data={"username": "Testuser",
                                      "first_name": "Martin",
                                      "last_name": "Paul",
                                      "email": "qqchose@mail.com",
                                      "password1": 'lfnedTTzpv244fjf',
                                      "password2": 'lfnedTTzpv244fjf'})

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

        response = self.client.get(reverse('register', args=(self.form,)))
        self.assertRedirects(response, '/login/')
