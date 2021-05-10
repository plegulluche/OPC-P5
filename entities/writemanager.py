import json

import mysql.connector
from mysql.connector import errorcode

import config
from datacleaner import Datacleaner

class Writemanager:


    def __init__(self):
        
        self.cnxvar = mysql.connector.connect(**config.userid) #variable containing the connector.connect.
        self.cnxcursor = self.cnxvar.cursor()                  #connection cursor. 
        self.data = Datacleaner()
            

    def writecategories(self):                  #for category we call Apimanager.createcategoryobject(Apimanager.getsixcategories()) , 
                                                            #An Apimanager instance need to be created beforehand.OR NOT ? (inside function ? )
        
        categoryapi = self.data.createcategoryobject()
        self.cnxvar                      #using with statement so the connection and the cursor are closed after usage.
        self.cnxcursor
        for categorie in categoryapi:
            query = "INSERT INTO Category (categoryName) VALUES (%s)"
            val = (categorie.categoryname)
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()
                
    
    def writeproduct(self):
        
        apiproducts = self.data.createproductobject()
        self.cnxvar
        self.cnxcursor
        for product in apiproducts:
            query = "INSERT INTO Product (productName, linkToURLOFF, nutriScore) VALUES (%s, %s, %s)"
            val = (product.productname, product.linktourl, product.nutriscore)
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()

    def writeshops(self):
        
        shops = self.data.createshopobjects()
        self.cnxvar
        self.cnxcursor
        for shop in shops:
            query = "INSERT INTO Shops (shopName) VALUES (%s)"
            val = (shop.shopname)
            self.cnxcursor.execute(query, val)
            self.cnxvar.commit()
        
        self.cnxvar.close()
            