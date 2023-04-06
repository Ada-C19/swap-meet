from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
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
        for items in self.inventory:
            if id == items.id:
                return items
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        their_item = other_vendor.inventory[0]
        my_item = self.inventory[0]

        self.remove(my_item)
        self.add(their_item)

        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        
        return True
    
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.get_category() == category:
                item_list.append(item)
        return item_list
    
    def get_best_by_category(self, category):
        item_list = self.get_by_category(category)
        highest_condition_value = 0
        highest_condition_item = None

        if not item_list:
            return highest_condition_item
        
        for item in item_list:
            if item.condition > highest_condition_value:
                highest_condition_value = item.condition
                highest_condition_item = item
        
        return highest_condition_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not other_vendor.get_by_category(my_priority):
            return False
        if not self.get_by_category(their_priority):
            return False
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        self.swap_items(other_vendor, my_item, their_item)
        return True









        

    



        