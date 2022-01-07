from django.test import TestCase
from django.test import Client
from django.urls import reverse
from ..models import Product, Category


class TestViews(TestCase):
    """Tests for products.views"""

    def setUp(self):

        Product.objects.create(category=Category.objects.create(category_name="Pate a tartiner"),
                               product_name='Nutella',
                               nutriscore='E',
                               nutri_values='expected_values',
                               off_url='expectedurlforproduct.com/prdct.png',
                               img_url='expectedurlforimg.com/img.png')
        self.product = Product.objects.get(product_name='Nutella')

    def test_search_sub(self):
        """Finds a result"""

        client = Client()
        keyword = '/?q=nutella'
        response = client.get(reverse('search_results', args=(keyword,)))
        self.assertEqual(response.status_code, 200)

    # def test_search_sub_no_result(self):
    #     pass

    # def test_sub_details_do_not_exist(self):
    #     pass

    # def test_save_sub(self):
    #     pass

    # def test_save_sub_already_saved(self):
    #     pass

    # def test_favorite_sub(self):
    #     pass

    # def test_no_favorite_sub(self):
    #     pass
