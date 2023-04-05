from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for thing in self.inventory:
            if item == thing:
                self.inventory.remove(thing)
                return item
        return False
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if len(other_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
        else:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, item_category):
        item_in_category = []
        for item in self.inventory:
            if item.name == item_category:
                item_in_category.append(item)
        return item_in_category
    
    def get_best_by_category(self, category_name):
        list_of_items = self.get_by_category(category_name)

        if len(list_of_items) == 0:
            return None
        else:
            return max(list_of_items, key = lambda x: x.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_requested_category = other_vendor.get_best_by_category(my_priority)
        their_requested_category= self.get_best_by_category(their_priority)

        if not their_requested_category or not my_requested_category:
            return False
        else:
            self.swap_items(other_vendor, their_requested_category, my_requested_category)
            return True
