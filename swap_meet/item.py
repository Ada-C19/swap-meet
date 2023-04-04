import uuid as u

class Item:
    """ Initiate Item class for a specific object in inventory. """

    def __init__ (self, id=None):
        """ Assign a unique id to each item. """
        self.name = 'Item'
        self.id = u.uuid4() if id is None else id
    
    def get_category(self):
        """ Return the item's class name as a string. """
        return self.name
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."


