
class Vendor:
    
    def __init__(self, inventory = []):
        self.inventory = inventory

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
    
    def add(self, x):
        self.inventory.append(x)
        return x
    
    def get_by_id(self, element):
        if element in self.inventory:
            return element
        else: 
            return None



