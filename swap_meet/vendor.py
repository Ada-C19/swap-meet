class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item_avail = True if my_item in self.inventory else False
        their_item_avail = True if their_item in other_vendor.inventory else False

        if not my_item_avail or not their_item_avail:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)
        
        self.add(their_item)
        other_vendor.add(my_item)
        
        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]
        
        self.remove(self_first_item)
        self.add(other_first_item)
        
        other_vendor.remove(other_first_item)
        other_vendor.add(self_first_item)

        return True
        
    def get_by_category(self, category):
        if not self.inventory:
            return None
        
        matches = []

        for item in self.inventory:
            if item.get_category() == category:
                matches.append(item)
        
        return matches
    
    def get_best_by_category(self, category):
        """
        If there are no matches, matches will either be
        None or [], both can be used in the conditional
        to return None - otherwise we can continue with
        matches.
        """
        matches = self.get_by_category(category)
        
        if not matches:
            return None
        
        return max(matches, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False
        
        self.swap_items(other_vendor, my_best, their_best)

        return True
        