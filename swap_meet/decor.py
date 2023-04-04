""" Initiation of class Decor. """

from .item import Item

class Decor(Item):  
    """ Initiation decor class for specific items in inventory. """ 
    def __init__ (self, id=None, width=0, length=0, condition=0.0):
        """ Item decor initiated with width and length of zero.  """
        super().__init__(id, condition)
        self.name = "Decor"
        self.width = width
        self.length = length

    def __str__(self):
        """ Stringify an instance of class Decor. """
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."
