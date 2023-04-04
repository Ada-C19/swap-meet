""" Initiation of class Vendor """

class Vendor:
    """ docstring about class vendor """
    def __init__(self, inventory=None):
        """ Initiate class vendor with empty inventory. """
        self.name = 'Vendor'
        self.inventory = [] if inventory is None else inventory

    def add (self, item):
       """ Adds an item to inventory and returns the added item """
       self.inventory.append(item)
       return item


    def remove (self, item):
        """ Remove one matching item from the 'inventory' and returns it. Returns False if no matching item. """
        for i, k in enumerate(self.inventory):
          if k == item:
            self.inventory.pop(i)
            return item
        return False

    def get_by_id(self, id):
        """ docstring for get_by_id """
        for item in self.inventory:
            if item.id == id:
                return item
        return None

# - Instances of `Vendor` have an instance method named `get_by_id`
#   - This method takes one argument: an integer, representing an `Item`'s `id`
#   - This method returns the item with a matching `id` from the inventory
#   - If there is no matching item in the `inventory`, the method should explicitly return `None`