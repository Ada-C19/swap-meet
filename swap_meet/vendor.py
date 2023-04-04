from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory[self.inventory.index(my_item)] = their_item
        other_vendor.inventory[other_vendor.inventory.index(their_item)] = my_item
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items
    
    def get_best_by_category(self, category):
        if not self.inventory:
            return None
        
        item_best_condition = self.inventory[0]
        CATEGORY = self.get_by_category(category)

        if not CATEGORY:
            return None
        
        for item in CATEGORY:
            if item.condition > item_best_condition.condition:
                item_best_condition = item

        return item_best_condition
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True
    