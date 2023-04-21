from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not self.inventory or item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        try:
            return [item for item in self.inventory if item.id == id][0]
        except IndexError:    
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
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, category):
        same_category_items = [item for item in self.inventory if item.get_category() == category]
        return same_category_items
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)

        if not items:
            return None
        
        best = items[0]
        for item in items:
            if item.condition > best.condition:
                best = item
        return best
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        vendor_item_self_wants = other_vendor.get_best_by_category(my_priority) 
        self_item_vendor_wants = self.get_best_by_category(their_priority)
        
        if not vendor_item_self_wants or not self_item_vendor_wants:
            return False 
        
        self.swap_items(other_vendor, self_item_vendor_wants, vendor_item_self_wants)
        return True
    
    
    '''Optional part of projects'''
    
    def get_by_newest(self):
        '''Function returns most recently created item (latest version(youngest age)) from inventory.
            If year hasnt been given through argument, or inventory is empty - returns False.'''
            
        if not self.inventory:
            return None
        
        latest = None
        for item in self.inventory:
            if not item.year:
                continue
            if latest is None:
                latest = item
            elif item.calculate_age() < latest.calculate_age():
                latest = item
                
        return latest
    
    def swap_by_newest(self, other_vendor):
        my_item = self.get_by_newest()
        their_item = other_vendor.get_by_newest()
        
        if not my_item or not their_item:
            return False
        
        self.swap_items(other_vendor, my_item, their_item)
        return True