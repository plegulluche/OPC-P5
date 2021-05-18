import requests



class Apimanager:
    """This class makes the API requests and transform the response into objects."""

    def __init__(self):
        self.rawcategorydata = None
        self.rawproductdata = None
        self.getcategory()
        self.getproductbycategory()

    def getcategory(self):
        """Method to make the API call to get categories and get the response in a json format."""
        response = requests.get(
            "https://fr.openfoodfacts.org/categories.json"
        )  # send the request to the API to get all categories.

        data = (
            response.json()
        )  # all our categories returned in a dict in a .json object.

        self.rawcategorydata = data

    def geteightcategories(self):
        """Method that takes the data from getcategory and extract the name of the 6 categories with the most products"""

        eightcategories = []

        sortedkeys = sorted(
            self.rawcategorydata["tags"], key=lambda x: x["products"], reverse=True
        )  # sorting categories by products in decending order to fetch the first 6 with highest values
        for elems in sortedkeys[
            :8
        ]:  # itering through the 6 firest elements of the list of dict in sortedkeys.
            keys = ["name"]  # defining the keys to go through
            values = list(map(elems.get, keys))  # putting the values fetched in a list.
            for items in values:
                eightcategories.append(items)

        return eightcategories

    def getproductbycategory(self):
        """
        Method of the Apimanager class, takes a list of category as argument,
        and iterate through them to get 100 products of each category from the api in a json format and put em in a dict.

        """
        eight = self.geteightcategories()
        productsliste = []
        for category in eight:
            print("ROG DEBUG: one category:", category)

            for page in range(1, 3, 1):
                print("PIER DEBUG: page:", page)
                r2 = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&tag_contains_1=contains&tag_1=france&page_size=500&fields=url,categories_tags_fr,product_name,stores_tags,nutriscore_grade&tagtype_1=purchase_places&sort_by=unique_scans_n&json=1&page={}".format(
                        category, page
                    )
                )
                dataproducts = r2.json()
                print("PIERR DEBUG: pagecount:", dataproducts["page_count"])
                if dataproducts["page_count"] is None:
                    continue
                else:
                    for items in dataproducts["products"]:
                        productsliste.append(items)

        self.rawproductdata = productsliste
