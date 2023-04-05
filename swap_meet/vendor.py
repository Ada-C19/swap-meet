class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory  =  []
        else:
            self.inventory  = inventory
            
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
        
    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
        
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
            
    
    
    
    
    
    
#     class Vendor:
# def __init__(self)

# def get_by_id(self, item_id)   #takes one argument: an integer, representing an `Item`'s `id` -> 
# ween vendor and item for this method?
# return item_in_inventor_with_item_id or None