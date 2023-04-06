
import uuid

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        
    
    def get_by_category(self, category):
        result = [item for item in self.inventory if item.get_category() == category]
        return result 


    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        
        if not items:
            return None
        return max(items, key=lambda item: item.condition)     


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if  not self.get_best_by_category(their_priority) or not other_vendor.get_best_by_category(my_priority):
            return False

        return self.swap_items(other_vendor, self.get_best_by_category(their_priority), other_vendor.get_best_by_category(my_priority))
    