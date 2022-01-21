from django.test import TestCase
from products.models import Category, Product, Favorite
from django.contrib.auth.models import User


class ModelsTests(TestCase):
    """Tests models from products app"""

    def create_category_model(self):
        """Creates a Category instance"""

        return Category.objects.create(category_name="Pate a tartiner")

    def test_create_category_model(self):
        """Tests the creation of a Category instance"""

        before_creation = Category.objects.count()
        c = self.create_category_model()
        after_creation = Category.objects.count()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(after_creation, before_creation+1)

    def create_product_model(self):
        """Creates a Product instance"""

        p = Product.objects.create(category=Category.objects.create(category_name="Pate a tartiner"),
                                   product_name="Nutella",
                                   nutriscore="E",
                                   nutri_values={"sucre": "35",
                                                 "sel": "0"},
                                   off_url="test.com/testurl",
                                   img_url="test.com/testimage.png")
        return p

    def test_create_product_model(self):
        """Tests the creation of a Category instance"""

        before_creation = Product.objects.count()
        p = self.create_product_model()
        after_creation = Product.objects.count()
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(after_creation, before_creation+1)

    def test_create_favorite_model(self):
        """Tests the creation of a Favorite instance"""

        before_creation = Favorite.objects.count()
        p = self.create_product_model()
        u = User.objects.create_user('usertest',
                                     'myemail@test.com', 'testpwd')
        f = Favorite.objects.create(products=p, user=u)
        after_creation = Favorite.objects.count()
        self.assertTrue(isinstance(f, Favorite))
        self.assertEqual(after_creation, before_creation+1)
