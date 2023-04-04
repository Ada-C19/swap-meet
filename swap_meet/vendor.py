from swap_meet import item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            return item
        else:
            return False
    
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
            