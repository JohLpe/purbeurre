from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """manages category table"""

    category_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """manages search and display substitute table"""

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    nutri_values = models.TextField()
    off_url = models.URLField(max_length=150)
    img_url = models.URLField(max_length=150)

    def __str__(self):
        return self.product_name

    def transl_nutri_keys(nutri_dict):
        """translate the keys in nutri_values to french"""

        try:
            nutri_dict['Glucides (g)'] = nutri_dict.pop('carbohydrates_100g')
            nutri_dict['Energie (kcal)'] = nutri_dict.pop('energy-kcal_100g')
            nutri_dict['Matières grasses (g)'] = nutri_dict.pop('fat_100g')
            nutri_dict['Protéines (g)'] = nutri_dict.pop('proteins_100g')
            nutri_dict['Sel (g)'] = nutri_dict.pop('salt_100g')
            nutri_dict['Matières grasses saturées (g)'] = nutri_dict.pop('saturated-fat_100g')
            nutri_dict['Sucres (g)'] = nutri_dict.pop('sugars_100g')
            nutri_dict['Fibres (g)'] = nutri_dict.pop('fiber_100g')
        except Exception:
            pass


class Favorite(models.Model):
    """manages save and delete favorite products table"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "product number {} for user {}".format(self.product,
                                                      self.user)

    class Meta:
        unique_together = (("product", "user"),)
