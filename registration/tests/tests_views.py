from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from ..utils import NewUserForm


class TestsRegistrationView(TestCase):
    """Tests registration views.py"""

    def setUp(self):

        NewUserForm(data={"username": "Testuser",
                                 "first_name": "Martin",
                                 "last_name": "Paul",
                                 "email": "qqchose@mail.com",
                                 "password1": 'lfnedTTzpv244fjf',
                                 "password2": 'lfnedTTzpv244fjf'})

    def test_register_page(self):

        client = Client()
        response = client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):

        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):

        client = Client()
        response = client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
