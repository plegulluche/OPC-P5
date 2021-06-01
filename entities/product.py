class Product:
    """Product class"""

    def __init__(self, nutriscore, productname, linktourl, categories, shop, **kwargs):
        """Product class construtor, can take *arg"""

        self.nutriscore = nutriscore
        self.productname = productname
        self.linktourl = linktourl
        self.categories = categories
        self.shop = shop

    def __repr__(self):
        """display Product in console"""
        return f"{self.productname}"

    def __str__(self):
        """display Product object for print method"""
        return repr(self)
