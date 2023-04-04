from item import Item
class Vendor:
    def __init__(self):
        self.inventory = []
        
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
            if id == self.id:
                return item
        return None