class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        try:
            for i in range(len(self.inventory)):
                if self.inventory[i].id == id:
                    return self.inventory[i]
        except:
            return None