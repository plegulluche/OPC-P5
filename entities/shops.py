class Shops:
    """description of the shops class"""

    def __init__(self, name):
        """__init__ Method of the Shops class"""

        self.shopname = name

    def __repr__(self):
        """display Product in console"""
        return f"{self.shopname}"

    def __str__(self):
        """display Product object for print method"""
        return repr(self)
