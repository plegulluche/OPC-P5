import requests
from tqdm import tqdm


class Apimanager:
    """
    Class to fetch data from the Open
    Food Fact API.
    """

    def __init__(self):
        self.rawcategorydata = None
        self.rawproductdata = None
        self.getcategory()
        self.getproductbycategory()

    def getcategory(self):
        """
        Get category data from the API.

        Return a dictionnary of values.
        """

        response = requests.get("https://fr.openfoodfacts.org/categories.json")

        data = response.json()

        self.rawcategorydata = data

    def geteightcategories(self):
        """
        Exctract 8 categories with the most products
        from the category datas from getcategory().

        Return a list.
        """

        eightcategories = []

        sortedkeys = sorted(
            self.rawcategorydata["tags"], key=lambda x: x["products"], reverse=True
        )
        for elems in sortedkeys[:8]:
            keys = ["name"]
            values = list(map(elems.get, keys))
            for items in values:
                eightcategories.append(items)

        return eightcategories

    def getproductbycategory(self):
        """
        Get product from the API,
        return a list.
        """

        eight = self.geteightcategories()
        productsliste = []
        for category in eight:
            for page in tqdm(range(1, 5)):
                r2 = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
                    + "&tagtype_0=categories&tag_contains_0=contains&tag_0={}".format(
                        category
                    )
                    + "&tag_contains_1=contains&tag_1=france&page_size=500"
                    + "&fields=url,categories_tags_fr,product_name,stores_tags"
                    + ",nutriscore_grade&tagtype_1=purchase_places&sort_by="
                    + "unique_scans_n&json=1&page={}".format(page)
                )
                dataproducts = r2.json()
                if dataproducts["page_count"] is None:
                    continue
                else:
                    for items in dataproducts["products"]:
                        productsliste.append(items)

        self.rawproductdata = productsliste
