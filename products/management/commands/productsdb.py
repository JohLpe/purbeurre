from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product
from products.utils import AddProduct


class Command(BaseCommand):
    help = 'adds categories to database'

    def handle(self, *args, **options):
        api_access = AddProduct()
        try:
            for category in api_access.categorylist:
                category = api_access.value_cleaner(category)
                c = Category.objects.create(category_name=category)
        except Exception as e:
            print(e)
        for one_product in api_access.products_query():
            p = Product(category=Category.objects.get(category_name=one_product['category']),
                        product_name=one_product['product_name'],
                        nutriscore=one_product['nutriscore_grade'],
                        nutri_values=one_product['nutriments'],
                        off_url=one_product['url'],
                        img_url=one_product['image_url'])
            p.save()



# faire fusion des deux commandes
# faire la création sur une ligne Category.objects.create()
# mettre des try