from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
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
        
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        try:
            self.inventory.remove(my_item)
        except ValueError:
            return False
        try:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
        except ValueError:
            self.inventory.append(my_item)
            return False
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        other_vendor_first_item = other_vendor.inventory.pop(0)
        my_first_item = self.inventory.pop(0)
        other_vendor.inventory.append(my_first_item)
        self.inventory.append(other_vendor_first_item)
        return True
    
    def get_by_category(self, category):
        items_match_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_match_category.append(item)
        return items_match_category
    
    def get_best_by_category(self, category):
        items_match_category = self.get_by_category(category)
        best_condition = 0.0
        best_item = None
        for item in items_match_category:
            if float(item.condition_description()) > best_condition:
                best_condition = float(item.condition_description())
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item_category = self.get_best_by_category(their_priority)
        their_best_item_category = other_vendor.get_best_by_category(my_priority)
        if not my_best_item_category or not their_best_item_category:
            return False
        return self.swap_items(other_vendor, my_best_item_category, their_best_item_category)
