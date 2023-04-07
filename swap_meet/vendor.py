from swap_meet.item import Item
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item): 
        self.inventory.append(item)
        return item
 
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        return True


    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, their_first_item)

        return True
        
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category


    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None
        
        item_list = self.get_by_category(category)
        best_condition = 0
        best_item = item_list[0]

        for item in item_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
            my_best_item = self.get_best_by_category(their_priority)
            their_best_item = other_vendor.get_best_by_category(my_priority)
    
            return self.swap_items(other_vendor, my_best_item, their_best_item)