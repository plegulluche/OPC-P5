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

    def readproductnameorid(self,value):        #OK
        
        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = 0
            
         
        if isinstance(value, int):
            query = "SELECT productName FROM Product WHERE productID = %(prodid)s "
            prodcursor.execute(query, {"prodid" : value})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values
        
        
        if isinstance(value, str):
            query = "SELECT productID FROM Product WHERE productName = %(prodname)s "
            prodcursor.execute(query, {"prodname" : value})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values

        prodcursor.close()
        cnxvar.close()

        return retour

    def selectproductdata(self,idprod):           #OK
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

    def readshops(self,value):          #OK

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
        
    def readproductcateprod(self,value):         #OK
        
        cnxvar = mysql.connector.connect(**config.userid)    
        readcursor = cnxvar.cursor()
        retourids = []

        queryname = "SELECT categoryName FROM Category INNER JOIN ProductCategory ON Category.categoryID = ProductCategory.categoryID WHERE ProductCategory.productID = %(prodid)s "
        readcursor.execute(queryname, { "prodid" : value })
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids
                
    def readproductcatecate(self,value):             #OK

        cnxvar = mysql.connector.connect(**config.userid)    
        readcursor = cnxvar.cursor()
        retourids = []


        queryid = "SELECT productName FROM Product INNER JOIN ProductCategory ON Product.productID = ProductCategory.productID WHERE ProductCategory.categoryID = %(cateid)s "
        readcursor.execute(queryid, { "cateid" : value })
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductshopshop(self,value):    #OK
        
        cnxvar = mysql.connector.connect(**config.userid)    
        readcursor = cnxvar.cursor()
        retourids = []

        
        queryid = "SELECT shopName FROM Shops INNER JOIN ProductInShop ON Shops.shopID = ProductInShop.shopID WHERE ProductInShop.productID = %(prodid)s "
        readcursor.execute(queryid, { "prodid" : value })
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)
        
        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductshopproducts(self,value):    #OK

        cnxvar = mysql.connector.connect(**config.userid)    
        readcursor = cnxvar.cursor()
        retourids = []

        
        queryid = "SELECT productName FROM Product INNER JOIN ProductInShop ON Product.productID = ProductInShop.productID WHERE ProductInShop.shopID = %(shopid)s "
        readcursor.execute(queryid, { "shopid" : value })
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids


    def readsurrogate(self):     # a check et finir voir les retour du fetchall quand elements dans la table.
        
        cnxvar = mysql.connector.connect(**config.userid)    
        readcursor = cnxvar.cursor()
        retourids = []

        query = "SELECT * FROM Surrogate INNER JOIN Product ON Product.productID = Surrogate.productID AND Product.productID = Surrogate.surrogateID "
        readcursor.execute(query)
        for rows in readcursor.fetchall():
            for values in rows:
                retour = values

    def read5randomcate(self):           #OK
      
        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = []

        query = "SELECT categoryID FROM ProductCategory WHERE RAND() > 0.9 ORDER BY RAND() LIMIT 5"
        prodcursor.execute(query)
        for rows in prodcursor.fetchall():
            for values in rows:
                retour.append(values)

        prodcursor.close()
        cnxvar.close()

        return retour

    def read5randomproduct(self,category):

        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = []
        query = "SELECT productID FROM ProductCategory WHERE RAND() > 0.9 AND categoryID = %(cateid)s LIMIT 5"
        prodcursor.execute(query, { "cateid" : category })
        for rows in prodcursor.fetchall():
            for values in rows:
                retour.append(values)
        
        prodcursor.close()
        cnxvar.close()

        return retour