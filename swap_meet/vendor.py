

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
       self.inventory.append(item)
       return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
           self.inventory.remove(item)
           return item
        
    def get_by_id(self, id):
        for item in self.invetory:
            if item.id == id:
                return item
        return None
