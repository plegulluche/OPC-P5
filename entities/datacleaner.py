import json

from apimanager import Apimanager
from product import Product
from shops import Shops
from category import Category



class Datacleaner:


    def __init__(self):
        self.api = Apimanager()

        

    def extractcategoriesnames(self):
        """Method that takes the data from getcategory method and extract the name of the categories from the json object."""
        
        allcategories = []
        for allcategory in self.api.rawcategorydata["tags"]:     #loop through all category and put their name in a list.
            category = allcategory["name"]
            allcategories.append(category)
        
        return allcategories

    def createcategoryobject(self):       
        """Method that take a list as parameter and use the elements of that list to create category objects."""

        categoryobjectslist = []
        categories = self.extractcategoriesnames()
        for category in categories:
            categoryobjectslist.append(Category(str(category)))

        return categoryobjectslist

    def geteightcategories(self):
        """Method that takes the data from getcategory and extract the name of the 6 categories with the most products"""
        
        eightcategories = []
        
        sortedkeys = sorted(self.api.rawcategorydata["tags"], key = lambda x: x["products"],reverse = True)  # sorting categories by products in decending order to fetch the first 6 with highest values
        for elems in sortedkeys[:8]:           # itering through the 6 firest elements of the list of dict in sortedkeys.
            keys = ["name"]                    # defining the keys to go through
            values = list(map(elems.get, keys))   #putting the values fetched in a list.
            for items in values:
                eightcategories.append(items)
                 
        return eightcategories

    def createproductobject(self):
        """
        Method of the Apimanager class, to extract from the json response of the getproductcategory method,
        all the needed product attributes.Returns a dictionnary with the keys and corresponding values.

        """  
        
        productlist = []
        eight = self.geteightcategories()             # creating the list that will contain all our product objects.
        for index in range(len(eight)):        #itering through the length of the category list.
            categories = eight[index]          #using the index to fetch categories of the category list one by one.
            for products in self.api.rawproductdata["{}".format(categories)]:
                keys = ["categories_tags_fr", "url", "product_name", "nutriscore_grade", "stores_tags"]
                values = dict(categories = products.get(keys[0]),
                              linktourl = products.get(keys[1]),
                              nutriscore = products.get(keys[3]),
                              productname = products.get(keys[2]),
                              shop = products.get(keys[4]) 
                              )
                
                productlist.append(Product(nutriscore = values["nutriscore"], 
                                           productname = values["productname"], 
                                           linktourl = values["linktourl"], 
                                           categories = values["categories"],
                                           shop = values["shop"]))
        return productlist

    def getshopslist(self):

        self.api.rawproductdata
        shoplist = []
        eight = self.geteightcategories()
        for index in range(len(eight)):
            categories = eight[index]
            for products in self.api.rawproductdata["{}".format(categories)]:
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