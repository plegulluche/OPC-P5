import mysql.connector

import entities.config as config
from entities.apimanager import Apimanager as Apimanager
from entities.product import Product as Product
from entities.shops import Shops as Shops
from entities.category import Category as Category


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

        allcategories = []
        for allcategory in self.api.rawcategorydata[
            "tags"
        ]:  
            category = allcategory["name"]
            allcategories.append(category)

        return allcategories

    def createcategoryobject(self):

        categoryobjectslist = []
        categories = self.extractcategoriesnames()
        for category in categories:
            categoryobjectslist.append(Category(str(category)))

        return categoryobjectslist

    def createproductobject(self):

        productlist = []

        for products in self.api.rawproductdata:
            keys = [
                "categories_tags_fr",
                "url",
                "product_name",
                "nutriscore_grade",
                "stores_tags",
            ]
            values = dict(
                categories=products.get(keys[0]),
                linktourl=products.get(keys[1]),
                nutriscore=products.get(keys[3]),
                productname=products.get(keys[2]),
                shop=products.get(keys[4]),
            )
            if values["productname"] is not None:
                productlist.append(
                    Product(
                        nutriscore=values["nutriscore"],
                        productname=values["productname"],
                        linktourl=values["linktourl"],
                        categories=values["categories"],
                        shop=values["shop"],
                    )
                )
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

        return shoplist  

    def createshopobjects(self):

        shops = self.getshopslist()
        shopsobjectlist = []

        for shop in shops:
            shopsobjectlist.append(Shops(shop))

        return shopsobjectlist
