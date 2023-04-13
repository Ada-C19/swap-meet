from swap_meet.item import *

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        if not self.inventory:
            return None
        
        for item in self.inventory:
            if id == item.id:
                return item
        
    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_item, their_item)
        return True
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list

    def get_best_by_category(self, category):
        matching_category = self.get_by_category(category)
        return max(matching_category, default=None, key=lambda item: item.condition)

        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return None
        
        their_wanted_item = self.get_best_by_category(their_priority)
        my_wanted_item = other_vendor.get_best_by_category(my_priority)
        
        return self.swap_items(other_vendor, their_wanted_item, my_wanted_item)
    
    def get_newest(self):
        return min(self.inventory, key=lambda item: item.age)
    
    def swap_by_newest(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return None
        
        return self.swap_items(other_vendor, self.get_newest(), other_vendor.get_newest())
        