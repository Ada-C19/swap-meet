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
            if isinstance(id, Item):
                raise ValueError("id should be an int")


    def swap_items(self, other_vendor, my_item, their_item):
        if not self.inventory or not other_vendor.inventory:
            return False
        if their_item not in self.inventory and my_item not in other_vendor.inventory:
            my_index, their_index = self.inventory.index(my_item), other_vendor.inventory.index(their_item)
            self.inventory[my_index], other_vendor.inventory[their_index] = their_item, my_item
            return True
        return False
        
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory[0], other_vendor.inventory[0] = (other_vendor.inventory[0],                                                     self.inventory[0])
        return True
        
    def get_by_category(self, category):
        matching_items = []
        matching_items = [item for item in self.inventory if item.get_category() == category]
        if matching_items:
            return matching_items
        else:
            return None
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None
        return max(items, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            if self.swap_items(other_vendor, my_best_item, their_best_item):
                return True
        return False

    def get_best_by_newest(self, age):
        items = self.get_by_category(age)
        if not items:
            return None
        return min(items, key=lambda item: item.age)

    def swap_best_by_newest(self, other_vendor, my_item, their_item):
        my_best_item = self.get_best_by_newest(their_item)
        their_best_item = other_vendor.get_best_by_newest(my_item)
        if my_best_item and their_best_item:
            if self.swap_items(other_vendor, my_best_item, their_best_item):
                return True
        return False
        

        
