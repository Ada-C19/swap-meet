from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None): 
        #Why cannot pass test without inventory?
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
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
            if id == item.id:           
            # item.id Is this`item` refers to the string in the inventory?
                return item
        return None