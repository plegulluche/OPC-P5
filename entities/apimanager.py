import json
import requests
from operator import itemgetter

from category import Category
from product import Product
from shops import Shops

class Apimanager:
    """This class makes the API requests and transform the response into objects."""

    def __init__(self):
        self.rawcategorydata = None
        self.rawproductdata = {}
        self.getcategory()
       

    def getcategory(self):
        """Method to make the API call to get categories and get the response in a json format."""
        response = requests.get("https://fr.openfoodfacts.org/categories.json")  #send the request to the API to get all categories.
        
        data = response.json()  #all our categories returned in a dict in a .json object.
        
        self.rawcategorydata = data
    

    def extractcategoriesnames(self):
        """Method that takes the data from getcategory method and extract the name of the categories from the json object."""
        
        allcategories = []
        for allcategory in self.rawcategorydata["tags"]:     #loop through all category and put their name in a list.
            category = allcategory["name"]
            allcategories.append(category)
        
        return allcategories
   

    def geteightcategories(self):
        """Method that takes the data from getcategory and extract the name of the 6 categories with the most products"""
        
        eightcategories = []
        
        sortedkeys = sorted(self.rawcategorydata["tags"], key = lambda x: x["products"],reverse = True)  # sorting categories by products in decending order to fetch the first 6 with highest values
        for elems in sortedkeys[:8]:           # itering through the 6 firest elements of the list of dict in sortedkeys.
            keys = ["name"]                    # defining the keys to go through
            values = list(map(elems.get, keys))   #putting the values fetched in a list.
            for items in values:
                eightcategories.append(items)
                 
        return eightcategories

    def createcategoryobject(self):       
        """Method that take a list as parameter and use the elements of that list to create category objects."""

        categoryobjectslist = []
        categories = self.extractcategoriesnames()
        for category in categories:
            categoryobjectslist.append(Category(str(category)))

        return categoryobjectslist
           


    def getproductbycategory(self):
        """
        Method of the Apimanager class, takes a list of category as argument, 
        and iterate through them to get 100 products of each category from the api in a json format and put em in a dict.
        
        """
        eight = self.geteightcategories()
        productsdict = {}
        for category in eight:        
            # r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&sort_by=product_name&page_size=100&json=1".format(category))
            r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&tagtype_1=countries&tag_contains_1=contains&tag_1=fr&tagtype_2=purchase_places&tag_contains_2=contains&tag_2=france&sort_by=product_name&page_size=100&json=1".format(category)) 
            data = r.json()
            productsdict[category] = data

        self.rawproductdata = productsdict

    def createproductobject(self):
        """
        Method of the Apimanager class, to extract from the json response of the getproductcategory method,
        all the needed product attributes.Returns a dictionnary with the keys and corresponding values.

        """  
        
        self.getproductbycategory()
        productlist = []
        eight = self.geteightcategories()             # creating the list that will contain all our product objects.
        for index in range(len(eight)):        #itering through the length of the category list.
            categories = eight[index]          #using the index to fetch categories of the category list one by one.
            for products in self.rawproductdata["{}".format(categories)]["products"]:
                keys = ["categories", "url", "['agribalyse']['name_fr']", "nutrition_grades_tags", "stores_tags"]
                values = dict(categories = products.get(keys[0]),
                              linktourl = products.get(keys[1]),
                              nutriscore = products.get(keys[3]),
                              productname = products.get(keys[2]),
                              shop = products.get(keys[4]) 
                              )
                print(values)
                # productlist.append(Product(nutriscore = values["nutriscore"], 
                #                            linktourl = values["linktourl"], 
                #                            productname = values["productname"], 
                #                            categories = values["categories"],
                #                            shop = values["shop"]))
        return productlist

    def getshopslist(self):

        self.getproductbycategory()
        shoplist = []
        eight = self.geteightcategories()
        for index in range(len(eight)):
            categories = eight[index]
            for products in self.rawproductdata["{}".format(categories)]["products"]:
                keys = ["stores_tags"]                    
                values = map(products.get, keys)    
                for stores in values:
                    if stores is not None:
                        for store in stores:
                            if store not in shoplist:
                                shoplist.append(store)
        
        return shoplist           # returns a list of strings

    def createshopobjects(self):

        shops = self.getshopslist()
        shopsobjectlist = []

        for shop in shops:
            shopsobjectlist.append(Shops(shop))

        return shopsobjectlist