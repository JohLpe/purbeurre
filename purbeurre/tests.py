from django.test import TestCase, Client
from django.urls import reverse
from .views import index


class TestViews(TestCase):
    """Test purbeurre.views.py"""

    def test_whatever(self):

        client = Client()
        resp = client.get(reverse('homepage'))

        self.assertEqual(resp.status_code, 200)
