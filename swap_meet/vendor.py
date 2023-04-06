class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item,):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False 
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item 
        return None 
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        
        return items_in_category
    
    def get_best_by_category(self, category):
        best_condition_score = 0.0
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > best_condition_score:
                    best_item = item
                    best_condition_score = item.condition
        
        return best_item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False 
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        return True 

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        
        return self.swap_items(other_vendor, my_item, their_item)
        


