import json

import mysql.connector
from mysql.connector import errorcode

import config
from apimanager import Apimanager

class Writemanager:


    def __init__(self):
        
        self.cnxvar = mysql.connector.connect(**config.userid) #variable containing the connector.connect.
        self.cnxcursor = self.cnxvar.cursor()                  #connection cursor. 

    #TODO : method to get the category objects from the api manager (store em in a variable or use them as they are created ??? ) 
    #       and create a sql query to fill the corresponding table.    
    #TODO : Same as below for the products.
            

    def writecategories(self):                  #for category we call Apimanager.createcategoryobject(Apimanager.getsixcategories()) , 
                                                            #An Apimanager instance need to be created beforehand.OR NOT ? (inside function ? )
        api = Apimanager()
        apicate = api.createcategoryobject()
        self.cnxvar                      #using with statement so the connection and the cursor are closed after usage.
        self.cnxcursor
        primary = 0
        for categorie in apicate:
            categorie.primarykey = primary + 1
            primary += 1
            print(categorie.primarykey, categorie.categoryname)
            query = "INSERT INTO Category (categoryID, categoryName) VALUES (%s, %s)"
            val = (categorie.primarykey,categorie.categoryname)
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()
                
    
    def writeproduct(self):
        
        api = Apimanager()
        apiproducts = api.createproductobject()
        self.cnxvar
        self.cnxcursor
        primary = 0
        for product in apiproducts:
            product.primarykey = primary + 1
            primary += 1
            query = "INSERT INTO Product (productID, shopID, productName, linkToURLOFF) VALUES (%s, %s, %s, %s)"
            val = None    # a faire
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()

    def writeshops(self):
        pass
            