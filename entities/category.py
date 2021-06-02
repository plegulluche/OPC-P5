class Category:
    """Category class"""

    def __init__(self, category):
        """Constructor of the Category class.

        Keyword arguments:
        category -- a string
        """
        self.categoryname = category

    def __repr__(self):
        """display Category in console"""
        return f"{self.categoryname}"

    def __str__(self):
        """display Category object for print method"""
        return repr(self)
