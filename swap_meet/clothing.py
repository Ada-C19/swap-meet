""" Initiate class Clothing. """
from .item import Item

class Clothing(Item):
    '''Represents items of clothing'''
    def __init__(self, fabric="Unknown", id=None, condition=0.0, age=0):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        """ Extend Item's str method """
        return f"{super().__str__()} It is made from {self.fabric} fabric."
