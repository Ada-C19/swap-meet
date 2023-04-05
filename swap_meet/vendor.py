from .item import Item
from .decor import Decor
from .electronics import Electronics
from .clothing import Clothing

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
       self.inventory.append(item)
       return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
           self.inventory.remove(item)
           return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item


    def swap_items(self, other_vendor, my_item, their_item):
        if not self.inventory or not other_vendor.inventory:
            return False
        if their_item not in self.inventory:
            if my_item not in other_vendor.inventory:
                self.inventory.remove(my_item)
                other_vendor.inventory.remove(their_item)
                self.inventory.append(their_item)
                other_vendor.inventory.append(my_item)
                return True 
        
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
    

    def get_by_catergory(self, category):
        for item in self.inventory:
            if item.get_category() == category:
                return item
        # return None 

        
    
