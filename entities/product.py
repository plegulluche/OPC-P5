class Product:
    """Product class"""

    def __init__(self,nutriscore,productname,linktourl,categories,shop,**kwargs):
        """Product class construtor, can take *arg """

        self.nutriscore = nutriscore
        self.productname = str(productname)
        self.linktourl = linktourl
        self.categories = categories
        self.shop = shop


    def __repr__(self):
        """display Product in console"""  #TODO: make the repr method display the name of the product accessing the product name attribute.
        return self.productname
    
    def __str__(self):
        """display Product object for print method"""
        return repr(self)