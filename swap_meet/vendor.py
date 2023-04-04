from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=None):
        
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
            
    def add(self, item):
        
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None
        
    def get_by_category(self, category):
            
            matching_items = []
            
            for item in self.inventory:
                if item.category == category:
                    matching_items.append(item)
            return matching_items
        
    def get_best_by_category(self, category):
        best_item= None
        highest_condition = -1
        for item in self.inventory:
            if item.category() == category and item.condition>highest_condition:
                best_item = item
        return best_item
            
        if items.condition > highest_condition:
                highest_condition = items.condition
                best_item = items
        items=[item for item in self.inventory if item.get_category() == category]
        if len(items)>0:
            best_item = max(items, key)
        
    def get_by_id(self, id):
        
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.pop(0)
        other_vendor.inventory.pop(0)        
        return True
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if not my_best_item or not their_best_item:
            return False
        
        self.remove(my_best_item)
        other_vendor.add(my_best_item)
        
        other_vendor.remove(their_best_item)
        self.add(their_best_item)
        
        return True
        