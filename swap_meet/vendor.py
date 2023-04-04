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
        """ Get item with matching id from inventory, return None if not found """
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, vendor, my_item, their_item):
       """ Removes items from both vendor's inventories and swaps them. If item from one vendor is not present, no items will be swapped. """
       #Remove items from both inventories
       other_remove = vendor.remove(their_item)
       if not other_remove:
          return False
       self_remove = self.remove(my_item)
       if not self_remove:
          vendor.add(their_item)
          return False
       #Add items to both inventories
       self.add(their_item)
       vendor.add(my_item)
       return True
