class Vendor:
    def __init__(self):
        self.inventory = []

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
        else: 
            return False
        
        