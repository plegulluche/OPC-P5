import json

import mysql.connector
from mysql.connector import errorcode

import config
from datacleaner import Datacleaner

class Writemanager:


    def __init__(self):
           
        self.data = Datacleaner()
            

    def writecategories(self):                  
        
        categoryapi = self.data.createcategoryobject()
        cnxvar = mysql.connector.connect(**config.userid)                      
        catecursor = cnxvar.cursor()
        for categorie in categoryapi:
            query = "INSERT INTO Category(categoryName) VALUES (%(name)s)"
            val = (categorie.categoryname)
            catecursor.execute(query,{"name": val})
            cnxvar.commit()

        catecursor.close()   
        cnxvar.close()
                
    
    def writeproduct(self):
        
        apiproducts = self.data.createproductobject()
        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        for product in apiproducts:
            query = "INSERT INTO Product(productName, linkToURLOFF, nutriScore) VALUES (%(name)s, %(link)s, %(score)s)"
            val = (product.productname, product.linktourl, product.nutriscore)
            shopid = None
            prodcursor.execute(query,{"name" : val[0], "link" : val[1], "score" : val[2]})
            cnxvar.commit()

        prodcursor.close()
        cnxvar.close()

    def writeshops(self):
        
        shops = self.data.createshopobjects()
        cnxvar = mysql.connector.connect(**config.userid)
        shopcursor = cnxvar.cursor()
        for shop in shops:
            query = "INSERT INTO Shops(shopName) VALUES (%(name)s)"
            val = (shop.shopname)
            shopcursor.execute(query, {"name" : val})
            cnxvar.commit()
        
        shopcursor.close()
        cnxvar.close()
            