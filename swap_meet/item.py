""" Initiate class Item. """
import uuid as u

class Item:
    """ Initiate Item class for a specific object in inventory. """

    def __init__ (self, id=None, condition=0.0):
        """ Assign a unique id to each item. """
        self.name = self.__class__.__name__
        self.id = int(u.uuid4()) if id is None else int(id)
        self.condition = condition
    
    def get_category(self):
        """ Return the item's class name as a string. """
        return self.name
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        """Return description of item based on condition value."""
        if 0 <= self.condition < 1:
            return "very bad"
        if 1 <= self.condition < 2:
            return "poor"
        if 2 <= self.condition < 3:
            return "used"
        if 3 <= self.condition < 4:
            return "gently used"
        if 4 <= self.condition < 5:
            return "like new"
        if self.condition == 5:
            return "mint"


