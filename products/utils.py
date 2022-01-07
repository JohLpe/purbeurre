import requests


class AddProduct():
    """Fetch results from OpenFoodFacts API"""

    def __init__(self):

        self.categorylist = ['jus-multifruits', 'jus-d-orange',
                             'yaourts-nature', 'chocolats-noirs',
                             'chocolats-au-lait', 'chocolats-fourres',
                             'yaourts-aux-fruits', 'brioches-au-chocolat',
                             'pates-a-tartiner-au-chocolat',
                             'pates-a-tartiner-aux-noisettes',
                             'chocolats-en-poudre', 'brioches-pur-beurre',
                             'confitures-de-fruits-rouges',
                             'confitures-de-fruits-tropicaux',
                             'pains-de-mie', 'pains-complets']
        self.fields = ('product_name,image_url,'
                       'nutriscore_grade,nutriments,id,url')
        self.nutriments = ['carbohydrates_100g', 'energy-kcal_100g',
                           'fat_100g', 'fiber_100g', 'proteins_100g',
                           'salt_100g', 'saturated-fat_100g',
                           'sugars_100g']
        self.testcat = ['pains-de-mie', 'yaourts-nature']

    def value_cleaner(self, str_value):
        """Standardise string values"""

        str_value = str_value.replace('-', ' ')
        str_value = str_value.capitalize()
        return str_value

    def products_query(self):
        """Query to API and breakdown of results for products table"""

        products_list = []
        for category in self.categorylist:
            payload = {'action': 'process', 'tagtype_0': 'categories',
                       'tag_contains_0': 'contains', 'tag_0': category,
                       'page_size': 20, 'fields': self.fields, 'json': True}
            resp = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
                                params=payload)
            jresp = resp.json()
            for first_key in sorted(jresp.keys()):
                if first_key == 'products':
                    sorted_list = jresp[first_key]
                    for each_dict in sorted_list:
                        if len(sorted(each_dict.items())) != 6:
                            continue
                        else:
                            one_product = {}
                            if 'unknown' in each_dict.values() or\
                                    '' in each_dict.values():
                                continue
                            else:
                                for key, value in sorted(each_dict.items()):
                                    if key == 'url':
                                        one_product[key] = value
                                    elif key == 'nutriments':
                                        nutri_dict = {}
                                        for nutri_key, nutri_value in sorted(value.items()):
                                            if nutri_key in self.nutriments:
                                                nutri_dict[nutri_key] = str(nutri_value)
                                        one_product[key] = nutri_dict
                                    else:
                                        value = self.value_cleaner(value)
                                        one_product[key] = value
                                one_product['category'] = self.value_cleaner(category)
                                products_list.append(one_product)
        return products_list
