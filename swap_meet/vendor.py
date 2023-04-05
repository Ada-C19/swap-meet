from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)

        return item
    
    def remove(self, item):
        self.item = item
        
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self,id):
        
        for item in self.inventory:
            if item.id == id:
                return item
        return None


