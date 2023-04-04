from swap_meet.item import *

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
        # self.id = Item(self.id)

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
        
    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory: 
            return False
        if not their_item in other_vendor.inventory:
            return False
        # look at me later!
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory:
            return False
        if not other_vendor.inventory:
            return False
        my_item = self.inventory.pop(0)
        other_vendor.add(my_item)
        their_item = other_vendor.inventory.pop(0)
        self.add(their_item)
        #look at me too!
        # other_vendor.swap_items(self, their_item, my_item)
        # self.swap_items(other_vendor, my_item, their_item)
        return True
    
    def get_by_category(self, category):
        pass

    def get_best_by_category(self, category):
        pass

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        pass