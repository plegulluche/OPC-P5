class Category:
    """Category class"""

    def __init__(self,category):
        """method to create an object of the Category class, takes a single arg as string value."""
        self.categoryname = category


    def __repr__(self):
        """display Category in console"""
        return f"{self.categoryname}"
    
    def __str__(self):
        """display Category object for print method"""
        return repr(self)