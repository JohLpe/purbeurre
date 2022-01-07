from django.test import TestCase
from products.models import Category, Product, Favorite


class ModelsTests(TestCase):
    """Test models from products app"""

    def create_category_model(self):
        """Create a Category instance"""

        return Category.objects.create(category_name="Pate a tartiner")

    def test_create_category_model(self):
        """Test the creation of a Category instance"""

        c = self.create_category_model()
        self.assertTrue(isinstance(c, Category))

    def create_product_model(self):
        """Create a Product instance"""

        p = Product.objects.create(category=Category.objects.create(category_name="Pate a tartiner"),
                                   product_name="Nutella",
                                   nutriscore="E",
                                   nutri_values={"sucre": "35",
                                                 "sel": "0"},
                                   off_url="test.com/testurl",
                                   img_url="test.com/testimage.png")
        return p

    def test_create_product_model(self):
        """Test the creation of a Category instance"""

        p = self.create_product_model()
        self.assertTrue(isinstance(p, Product))
