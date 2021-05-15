import json

import mysql.connector
from mysql.connector import errorcode

import config
from datacleaner import Datacleaner

class Writemanager:


    def __init__(self):
           
        self.data = Datacleaner()
            

    def writecategories(self):                  
        
        categoryapi = self.data.categorylist
        cnxvar = mysql.connector.connect(**config.userid)                      
        catecursor = cnxvar.cursor()
        for categorie in categoryapi:
            query = "INSERT INTO Category(categoryName) VALUES (%(name)s)"
            val = (categorie.categoryname)
            catecursor.execute(query,{"name": val})
            cnxvar.commit()

        catecursor.close()   
        cnxvar.close()
        print("PIERR DEBUG: categories data inserted.")       
    
    def writeproduct(self):
        
        apiproducts = self.data.productslist
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
        print("PIERR DEBUG: product data inserted.")

    def writeshops(self):
        
        shops = self.data.shoplist
        cnxvar = mysql.connector.connect(**config.userid)
        shopcursor = cnxvar.cursor()
        for shop in shops:
            query = "INSERT INTO Shops(shopName) VALUES (%(name)s)"
            val = (shop.shopname)
            shopcursor.execute(query, {"name" : val})
            cnxvar.commit()
        
        shopcursor.close()
        cnxvar.close()
        print("PIERR DEBUG: shop data inserted.")

    def writeproductcategory(self):
        
        cnxvar = mysql.connector.connect(**config.userid)
        prodcatecursor = cnxvar.cursor()
        
        for products in self.data.productslist:                  #itering through list of products objects.  
            prodcate = products.categories
            print("PIERR DEBUG: one product", products)
            for categorie in prodcate:
                cate = categorie
                prodname = products.productname
                queryprod = "SELECT productID FROM Product WHERE productName = %(prodname)s "
                querycate = "SELECT categoryID FROM Category WHERE categoryName = %(cate)s "
                prodcatecursor.execute(queryprod, {"prodname" : prodname } )
                for rows in prodcatecursor.fetchall():
                    for values in rows:
                        prodid = values
                prodcatecursor.execute(querycate, {"cate" : cate})
                for rows in prodcatecursor.fetchall():
                    for values in rows:
                        cateid = values
                table = "ProductCategory"
                columnprod = "productID"
                columncate = "categoryID"
                queryinsert = f"INSERT IGNORE INTO {table}({columncate},{columnprod}) VALUES ({cateid}, {prodid})"
                prodcatecursor.execute(queryinsert)
                cnxvar.commit()
        
        prodcatecursor.close()
        cnxvar.close()

        print("PIERR DEBUG: product category insertion done.")

    def writeproductinshop(self):
        
        cnxvar = mysql.connector.connect(**config.userid)
        prodshopcursor = cnxvar.cursor()

        for products in self.data.productslist:
            prodshops = products.shop
            print("PIERR DEBUG: one product shop:", products)
            if prodshops is not None:
                for shops in prodshops:
                    shop = shops
                    prodname = products.productname
                    queryprod = "SELECT productID FROM Product WHERE productNAme = %(prodname)s "
                    queryshop = "SELECT shopID FROM Shops WHERE shopName = %(shop)s "
                    prodshopcursor.execute(queryprod, {"prodname" : prodname})
                    for rows in prodshopcursor.fetchall():
                        for values in rows:
                            prodid = values
                    prodshopcursor.execute(queryshop, {"shop" : shop})
                    for rows in prodshopcursor.fetchall():
                        for values in rows:
                            shopid = values
                    table = "ProductInShop"
                    columnprod = "productID"
                    columnshop = "shopID"
                    queryinsert = f"INSERT IGNORE INTO {table}({columnprod},{columnshop}) VALUES ({prodid}, {shopid})"
                    prodshopcursor.execute(queryinsert)
                    cnxvar.commit()

        prodshopcursor.close()
        cnxvar.close()

        print("PIERR DEBUG: product shop insertion done.")


                