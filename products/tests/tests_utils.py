from django.test import TestCase
from ..utils import AddProduct


class UtilsTests(TestCase):
    """Test AddProduct class from utils.py"""

    def test_products_query_get_list(self):
        """Verify results from AddProduct.products_query() is a list"""

        adc = AddProduct()
        self.assertEqual(type(adc.products_query()), list)

    def test_products_query_list_has_dictionaries(self):
        """Verify AddProduct.products_query() list result
        contains dictionaries"""

        adc = AddProduct()
        result_list = adc.products_query()
        problem = False
        for item in result_list:
            if type(item) == dict:
                return problem
            else:
                problem = True
                break
        self.assertIs(problem, False)

    def test_products_query_dict_have_right_keys(self):
        """Verify AddProduct.products_query() dictionaries have the
        expected keys"""

        adc = AddProduct()
        expected_keys = ('id', 'image_url', 'nutriments',
                         'nutriscore_grade', 'product_name',
                         'url', 'category')
        problem = False
        result_list = adc.products_query()
        for item in result_list:
            for key in item.keys():
                if key in expected_keys:
                    return problem
                else:
                    problem = True
                    break
        self.assertIs(problem, False)

    def test_value_cleaner(self):
        """Test AddProduct.value_cleaner()"""

        adc = AddProduct()
        str_test = "petit-beurres"
        self.assertEqual(adc.value_cleaner(str_test), "Petit beurres")
