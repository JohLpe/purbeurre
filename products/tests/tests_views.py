from django.test import TestCase, Client
from django.contrib import auth
from django.urls import reverse
from ..models import Product, Category
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Tests for products.views"""

    def setUp(self):

        self.client = Client()
        Product.objects.create(category=Category.objects.create(category_name="Pate a tartiner"),
                               product_name='Nutella',
                               nutriscore='E',
                               nutri_values='expected_values',
                               off_url='expectedurlforproduct.com/prdct.png',
                               img_url='expectedurlforimg.com/img.png')
        self.product = Product.objects.get(product_name='Nutella')
        self.user = User.objects.create_user('usertest', 'myemail@test.com', 'testpwd')

    def test_search_substitute(self):
        """Tests if search results page can be reached"""

        response = self.client.get(reverse('search_results') + '?q=nutella')
        self.assertEqual(response.status_code, 200)

    def test_detail_substitute(self):
        """Tests if a product's page can be reached"""

        product_id = self.product.id
        response = self.client.get(reverse('product_details', kwargs={'product_id': product_id}))
        self.assertEqual(response.status_code, 200)

    def test_detail_substitute_do_not_exist(self):
        """Tests url for a product that doesn't exist"""

        product_id = 35
        response = self.client.get(reverse('product_details', args=(product_id,)))
        self.assertEqual(response.status_code, 400)

    def test_favorite_sub_logged_user(self):
        """Tests if favorite page can be reached"""

        self.client.login(username='usertest', password='testpwd')
        self.assertTrue(self.user.is_authenticated)
        response = self.client.get(reverse('favorites'))
        self.assertEqual(response.status_code, 200)

    def test_favorite_sub_not_logged_user(self):
        """Tests that favorite page cannot be reached if not logged"""

        user = auth.get_user(self.client)
        response = self.client.get(reverse('favorites'))
        self.assertTrue(user.is_anonymous)
        self.assertEqual(response.status_code, 404)

    def test_redirect_after_saving_substitute(self):
        """Tests that user reaches the favorite page after saving a substitute"""

        product_id = self.product.id
        response = self.client.get(reverse('save', args=(product_id,)))
        self.assertRedirects(response, 'favorites')
