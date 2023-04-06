

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

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
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
            
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, my_item, their_item)
        else:
            return False
        
    def get_by_category(self, category):
        filtered_inventory = []
        for item in self.inventory:
            if item.get_category() == category:
                filtered_inventory.append(item)
        return filtered_inventory

    def get_best_by_category(self, category):
        category_inventory = self.get_by_category(category)
        if len(category_inventory) == 0:
            return None
        return max(category_inventory, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # get the best items in categories
        their_item = other_vendor.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        
        # return and or swap item if possible.
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other_vendor, my_item, their_item)
            return True
