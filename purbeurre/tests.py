from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test purbeurre.views.py"""

    def test_homepage(self):

        client = Client()
        resp = client.get(reverse('homepage'))

        self.assertEqual(resp.status_code, 200)
