import mysql.connector

import entities.config as config


class Readmanager:
    """
    Class that manage the reading of the database.
    Each method handle a very specific aspect of each table.
    Read the method doc for more infos.
    """

    def __init__(self):
        """
        Readmanager class constructor.
        """
        pass

    def readcategory(self, value):
        """
        Reads the Category table of the food database.

        :param : Id or name of a category
        :type : int or str
        :return : name of category as str if param is int
                  id of category as int if param is str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcatecursor = cnxvar.cursor()

        retour = None

        if isinstance(value, int):
            query = "SELECT categoryName FROM Category WHERE categoryID = %(cateid)s "
            readcatecursor.execute(query, {"cateid": value})
            for rows in readcatecursor.fetchall():
                for values in rows:
                    retour = values

        if isinstance(value, str):
            query = "SELECT categoryID FROM Category WHERE categoryName = %(name)s "
            readcatecursor.execute(query, {"name": value})
            for rows in readcatecursor.fetchall():
                for values in rows:
                    retour = values

        readcatecursor.close()
        cnxvar.close()

        return retour

    def readproductnameorid(self, value):
        """
        Read the product name only from Product table of the food database.

        :param : Id or name of the product
        :type : int or str
        :return : name of product as str if param is int
                  id of product as int if param is str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = 0

        if isinstance(value, int):
            query = "SELECT productName FROM Product WHERE productID = %(prodid)s "
            prodcursor.execute(query, {"prodid": value})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values

        if isinstance(value, str):
            query = "SELECT productID FROM Product WHERE productName = %(prodname)s "
            prodcursor.execute(query, {"prodname": value})
            for rows in prodcursor.fetchall():
                for values in rows:
                    retour = values

        prodcursor.close()
        cnxvar.close()

        return retour

    def selectproductdata(self, idprod):
        """
        Reads productname,nutriscore and url of a product from
        the Product table in food database.

        :param : product id
        :type : int
        :return : Tuple containing values as strings

        """
        cnxvar = mysql.connector.connect(**config.userid)
        selectcursor = cnxvar.cursor()
        retour = None

        query = "SELECT productName, nutriScore, linkToURLOFF from Product WHERE productID = %(prodid)s  "
        selectcursor.execute(query, {"prodid": idprod})
        for rows in selectcursor.fetchall():
            retour = rows

        selectcursor.close()
        cnxvar.close()

        return retour

    def readshops(self, shopidorname):
        """
        Read the shopname or the shopid from Shop table from the food database.

        :param : shopid or shopname
        :type : int or str
        :return : shopname as str or shopid as int

        """

        cnxvar = mysql.connector.connect(**config.userid)
        shopcursor = cnxvar.cursor()
        retour = None

        if isinstance(shopidorname, int):
            query = "SELECT shopName FROM Shops WHERE shopID = %(shopid)s "
            shopcursor.execute(query, {"shopid": shopidorname})
            for rows in shopcursor.fetchall():
                for values in rows:
                    retour = values

        if isinstance(shopidorname, str):
            query = "SELECT shopID FROM Shops WHERE shopName = %(shopname)s "
            shopcursor.execute(query, {"shopname": shopidorname})
            for rows in shopcursor.fetchall():
                for values in rows:
                    retour = values

        shopcursor.close()
        cnxvar.close()

        return retour

    def readproductcateprod(self, productid):
        """
        Read all the category name associated to the product in the
        ProductCategory table.

        :param : productid
        :type : int
        :return :  list of str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retourids = []

        queryname = (
            "SELECT categoryName FROM Category INNER JOIN ProductCategory "
            + "ON Category.categoryID = ProductCategory.categoryID WHERE ProductCategory.productID = %(prodid)s "
        )
        readcursor.execute(queryname, {"prodid": productid})
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductcatecateid(seld, productid):
        """
        Read all the category id associated to the product in the
        ProductCategory table.

        :param : productid
        :type : int
        :return : list of int
        """
        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retourids = []

        query = "SELECT categoryID FROM ProductCategory WHERE productID = %(prodid)s "
        readcursor.execute(query, {"prodid": productid})
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductcatecate(self, categoryid):
        """
        Read the ProductCategory table inside food database,
        and extract the product names assiociated with the category id
        in the parameter.

        :param : category id
        :type : int
        :return : list of str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retourids = []

        queryid = (
            "SELECT productName FROM Product INNER JOIN "
            + "ProductCategory ON Product.productID = ProductCategory.productID "
            + "WHERE ProductCategory.categoryID = %(cateid)s "
        )
        readcursor.execute(queryid, {"cateid": categoryid})
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductshopshop(self, productid):
        """
        Read the ProductShop table from food database and extract
        the shopname corresponding to the product id in the param.

        :param : productid
        :type : int
        :return : list of str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retourids = []

        queryid = (
            "SELECT shopName FROM Shops INNER JOIN "
            + "ProductInShop ON Shops.shopID = ProductInShop.shopID"
            + " WHERE ProductInShop.productID = %(prodid)s "
        )
        readcursor.execute(queryid, {"prodid": productid})
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readproductshopproducts(self, shopid):
        """
        Read the ProductInShop table and extract all the products
        names assiociated to the shopid in param.

        :param : shopid
        :type : int
        :return : list of str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retourids = []

        queryid = (
            "SELECT productName FROM Product INNER JOIN "
            + "ProductInShop ON Product.productID = "
            + "ProductInShop.productID WHERE ProductInShop.shopID = %(shopid)s "
        )
        readcursor.execute(queryid, {"shopid": shopid})
        for rows in readcursor.fetchall():
            for values in rows:
                retourids.append(values)

        readcursor.close()
        cnxvar.close()

        return retourids

    def readsurrogate(self):
        """
        Read the Surrogate table in the food database.
        Fetch the product and their assiociated surrogate.

        :return : list of tuples
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retour = []

        query = "SELECT productID, surrogateID FROM Surrogate "
        readcursor.execute(query)
        for rows in readcursor.fetchall():
            retour.append(rows)

        readcursor.close()
        cnxvar.close()

        return retour

    def read5randomcate(self):
        """
        Read the Category table from food database and select
        5 random category id from it.

        :return : list of int
        """

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

    def read5randomproduct(self, category):
        """
        Read the ProductCategory table in the food database and fetch
        5 random products from the category in param.

        :param : category id
        :type : int
        :return : list of int
        """

        cnxvar = mysql.connector.connect(**config.userid)
        prodcursor = cnxvar.cursor()
        retour = []
        query = "SELECT productID FROM ProductCategory WHERE categoryID = %(cateid)s ORDER BY RAND() LIMIT 5"
        prodcursor.execute(query, {"cateid": category})
        for rows in prodcursor.fetchall():
            for values in rows:
                retour.append(values)

        prodcursor.close()
        cnxvar.close()

        return retour

    def readsamecate(self, valuelist):
        """
        Read ProductCategory table and fetch all product with the same
        categories as the ones in the list of param.

        :param : list of category id
        :type : list of int
        :return : list of int
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retour = []
        query = "SELECT productID FROM ProductCategory WHERE categoryID = %(cateid0)s "
        for iter in range(1, len(valuelist)):
            query = (
                query
                + f" UNION SELECT productID FROM ProductCategory WHERE categoryID = %(cateid{iter})s"
            )
        dicovaluesquery = {}
        for iters in range(len(valuelist)):
            dicovaluesquery[f"cateid{iters}"] = valuelist[iters]
        readcursor.execute(query, dicovaluesquery)
        for rows in readcursor.fetchall():
            for values in rows:
                retour.append(values)

        readcursor.close()
        cnxvar.close()

        return retour

    def readnutriscore(self, productid):
        """
        Read Product table from food database,
        and fetch the nutriscore of the product corresponding to
        the id in param.

        :param : product id
        :type : int
        :return : str
        """

        cnxvar = mysql.connector.connect(**config.userid)
        readcursor = cnxvar.cursor()
        retour = None
        query = "SELECT nutriScore FROM Product WHERE productID = %(prodid)s "
        readcursor.execute(query, {"prodid": productid})
        for rows in readcursor.fetchall():
            for values in rows:
                retour = str(values)

        readcursor.close()
        cnxvar.close()

        return retour
