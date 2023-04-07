""" Initiate class Item. """
import uuid as u

class Item:
    """ Initiate Item class for a specific object in inventory. """

    def __init__ (self, id=None, condition=0.0, age=0):
        """ Assign a unique id to each item. """
        if not (isinstance(id, int) or id is None):
            raise TypeError("IDs must be integers!")
        self.id = int(u.uuid4()) if id is None else int(id)

        if not (isinstance(condition, (int, float))):
            raise TypeError("Condition must be numeric!")
        self.condition = condition

        if not (isinstance(age, (int, float))):
            raise TypeError("Age (in years) must be numeric!")
        self.age = int(age)
    
    def get_category(self):
        """ Return the item's class name as a string. """
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        """Return description of item based on condition value."""
        conditions = {
            0: "very bad",
            1: "poor",
            2: "used",
            3: "gently used",
            4: "like new",
            5: "mint"
        }

        return conditions[int(self.condition)]


