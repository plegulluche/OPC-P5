import mysql.connector

import config
from apimanager import Apimanager
from product import Product
from shops import Shops
from category import Category



class Datacleaner:


    def __init__(self):

        self.api = 0
        cnxvar = mysql.connector.connect(**config.userid)
        dbcursor = cnxvar.cursor()
        query = "SELECT * FROM Shops"
        dbcursor.execute(query)
        if dbcursor.fetchall() == []:
            dbcursor.close()
            cnxvar.close()
            self.api = Apimanager()
        
        self.productslist = self.createproductobject()
        self.categorylist = self.createcategoryobject()
        self.shoplist = self.createshopobjects()
        

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

    
    def createproductobject(self):
        """
        Method of the Apimanager class, to extract from the json response of the getproductcategory method,
        all the needed product attributes.Returns a dictionnary with the keys and corresponding values.

        """  
        
        productlist = []
            
        for products in self.api.rawproductdata:
            keys = ["categories_tags_fr", "url", "product_name", "nutriscore_grade", "stores_tags"]
            values = dict(categories = products.get(keys[0]),
                            linktourl = products.get(keys[1]),
                            nutriscore = products.get(keys[3]),
                            productname = products.get(keys[2]),
                            shop = products.get(keys[4]) 
                            )
            if values['productname'] is not None:
                productlist.append(Product(nutriscore = values["nutriscore"], 
                                            productname = values["productname"], 
                                            linktourl = values["linktourl"], 
                                            categories = values["categories"],
                                            shop = values["shop"]))
        return productlist

    def getshopslist(self):

        self.api.rawproductdata
        shoplist = []       
        for products in self.api.rawproductdata:           
            keys = "stores_tags"                    
            values = products.get(keys)           
            if values is not None:
                for store in values:                   
                    if store not in shoplist:
                        shoplist.append(store)
        
        return shoplist           # returns a list of strings

    def createshopobjects(self):

        shops = self.getshopslist()
        shopsobjectlist = []

        for shop in shops:
            shopsobjectlist.append(Shops(shop))

        return shopsobjectlist