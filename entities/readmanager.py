from os import link
import mysql.connector

import config

class Readmanager():

    def __init__(self):
        pass

    def readcategory(self,value):
        '''Takes one parameter.
           Returns
        '''   
        cnxvar = mysql.connector.connect(**config.userid)
        readcatecursor = cnxvar.cursor()
        retour = None

        if isinstance(value, int):
            query = "SELECT categoryName FROM Category WHERE categoryID = %(cateid)s"
            readcatecursor.execute(query, {"cateid" : value})
            for rows in readcatecursor.fetchall():
                for values in rows:
                    retour = values

        if isinstance(value, str):
            query = "SELECT categoryID FROM Category WHERE categoryName = %(name)s"
            readcatecursor.execute(query, {"name" : value})
            for rows in readcatecursor.fetchall():
                for values in rows:
                    retour = values
        

        readcatecursor.close()
        cnxvar.close()
        return retour

    def readproductnameorid(self,id=0,name=0):
        """
        *args = [id] , [name].
        """
        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = 0
            
        valueid = id   #this block takes a number and fetch prod name by id
        if valueid != 0 and name ==0:
            query = "SELECT productName FROM Product WHERE productID = %(prodid)s "
            prodcursor.execute(query, {"prodid" : valueid})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values
        
        valuename = name  #this block takes a string value and fetch prod id by name
        if valuename != 0 and id == 0:
            query = "SELECT productID FROM Product WHERE productName = %(prodname)s "
            prodcursor.execute(query, {"prodname" : valuename})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values

        prodcursor.close()
        cnxvar.close()
        return retour

    def selectproductdata(self,idprod):
        """
        param in that order: prodid = "productID"
                             nutri = "nutriScore"
                             name = "productName"
                             link = "linkToURLOFF"
        cas d'utilisation : -affichage des données du produit
        besoins : link , nutriscore, nom.
        """
        cnxvar = mysql.connector.connect(**config.userid)
        selectcursor = cnxvar.cursor()
        
        query = "SELECT productName, nutriScore, linkToURLOFF from Product WHERE productID = %(prodid)s  "
        selectcursor.execute(query, { "prodid" : idprod})
        for rows in selectcursor.fetchall():
            print(rows)
            for values in rows:
                print(values)

        

    def readshops(self,value):

        cnxvar = mysql.connector.connect(**config.userid)
        shopcursor = cnxvar.cursor()
        retour = None

        if isinstance(value, int):
            query = "SELECT shopName FROM Shops WHERE shopID = %(shopid)s "
            shopcursor.execute(query, {"shopid" : value})
            for rows in shopcursor.fetchall():
                for values in rows:
                    retour = values
        
        if isinstance(value, str):
            query = "SELECT shopID FROM Shops WHERE shopName = %(shopname)s "
            shopcursor.execute(query, {"shopname" : value})
            for rows in shopcursor.fetchall():
                for values in rows:
                    retour = values
        
        shopcursor.close()
        cnxvar.close()
        return retour
        
    def readproductcate(self):
        pass
    def readproductshop(self):
        pass
    def readsurrogate(self):
        pass