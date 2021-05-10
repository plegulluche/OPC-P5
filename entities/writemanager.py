import json

import mysql.connector
from mysql.connector import errorcode

import config
from datacleaner import Datacleaner

class Writemanager:


    def __init__(self):
        
        self.cnxvar = mysql.connector.connect(**config.userid) #variable containing the connector.connect.
        self.cnxcursor = self.cnxvar.cursor()                  #connection cursor. 

            

    def writecategories(self):                  #for category we call Apimanager.createcategoryobject(Apimanager.getsixcategories()) , 
                                                            #An Apimanager instance need to be created beforehand.OR NOT ? (inside function ? )
        data = Datacleaner()
        categoryapi = data.createcategoryobject()
        self.cnxvar                      #using with statement so the connection and the cursor are closed after usage.
        self.cnxcursor
        for categorie in apicate:
            query = "INSERT INTO Category (categoryName) VALUES (%s)"
            val = (categorie.categoryname)
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()
                
    
    def writeproduct(self):
        
        data = Datacleaner()
        apiproducts = data.createproductobject()
        self.cnxvar
        self.cnxcursor
        primary = 0
        for product in apiproducts:
            product.primarykey = primary + 1
            primary += 1
            query = "INSERT INTO Product (productName, linkToURLOFF) VALUES (%s, %s, %s, %s)"
            val = None    # a faire
            self.cnxcursor.execute(query,val)
            self.cnxvar.commit()

        self.cnxvar.close()

    def writeshops(self):
        pass
            