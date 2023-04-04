""" Initiation of class Electronics """
from .item import Item

class Electronics(Item):
    """ Represents electronic items. """
    def __init__(self, type="Unknown", id=None, condition=0.0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        """Extend Item's string method"""
        return f"{super().__str__()} This is a {self.type} device."
