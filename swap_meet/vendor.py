class Vendor:
    
    def __init__(self,inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory 

    def add (self, item):
        self.inventory.append(item)
        return item 
    
    def remove (self, item):
        try:  
            self.inventory.remove(item)
            return item 
        except ValueError: 
            return False 
    
    def get_by_id(self, integer): 
        for item in self.inventory: 
            if integer == item.id: 
                return item
        return None