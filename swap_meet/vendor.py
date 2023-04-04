
class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
    
    def add(self,element):
        self.inventory.append(element)
        return element
    
    def get_by_id(self, id):
        for element in self.inventory:
            if id == element.id:
                return element
        return None

