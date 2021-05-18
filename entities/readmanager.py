import mysql.connector

import config

class Readmanager():

    def __init__(self):
        pass

    def readcategory(self,value):                  #OK 
        
        cnxvar = mysql.connector.connect(**config.userid)
        readcatecursor = cnxvar.cursor()

        retour = None

        if isinstance(value, int):
            query = "SELECT categoryName FROM Category WHERE categoryID = %(cateid)s "
            readcatecursor.execute(query, {"cateid" : value})
            for rows in readcatecursor.fetchall():
                for values in rows:   
                    retour = values


        if isinstance(value, str):
            query = "SELECT categoryID FROM Category WHERE categoryName = %(name)s "
            readcatecursor.execute(query, {"name" : value})
            for rows in readcatecursor.fetchall():
                for values in rows:
                    retour = values
        

        readcatecursor.close()
        cnxvar.close()

        return retour

    def readproductnameorid(self,value):
        """
        *args = [id] , [name].
        """
        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = 0
            
         
        if isinstance(value, int):
            query = "SELECT productName FROM Product WHERE productID = %(prodid)s "
            prodcursor.execute(query, {"prodid" : value})
            for rows in prodcursor.fetchall():
                print(rows)
                for values in rows:
                    retour = values
        
        
        if isinstance(value, str):
            query = "SELECT productID FROM Product WHERE productName = %(prodname)s "
            prodcursor.execute(query, {"prodname" : value})
            for rows in prodcursor.fetchall():
                print(rows)
                for values in rows:
                    retour = values

        prodcursor.close()
        cnxvar.close()

        return retour

    def selectproductdata(self,idprod):
        """

        Takes one param : INT (productID)
        Return : Tuple containing values as strings

        """
        cnxvar = mysql.connector.connect(**config.userid)
        selectcursor = cnxvar.cursor()
        
        query = "SELECT productName, nutriScore, linkToURLOFF from Product WHERE productID = %(prodid)s  "
        selectcursor.execute(query, { "prodid" : idprod})
        for rows in selectcursor.fetchall():   # return a tuple containing string values. 
            values = rows

        selectcursor.close()
        cnxvar.close()

        return values

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
        """productid = from product.productID
           categoryid = from category.categoryID
            

        """
        #faire un select de l'union ou jointure entre l id de la table prodcut cate et les tables product et category 
        #une methode si on a l'id de la cate et on veut les produits correspondants. 
        #une methode si on a l'id du produit et on veut les cate correpondantes.
        pass

    def readproductshop(self):
        #comme au dessus mais pour product et shop.
        pass

    def readsurrogate(self):
        
        #une methode qui va lire toutes les entrees de table et les afficher.
        pass

    