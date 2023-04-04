""" Initiate class Clothing. """
from .item import Item

class Clothing(Item):
    '''Represents items of clothing'''
    def __init__(self, fabric="Unknown", id=None, condition=0.0):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        """ Override """
        return f"{super().__str__()} It is made from {self.fabric} fabric."
