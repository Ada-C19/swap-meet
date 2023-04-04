class Vendor:
    
    # constructor for the vendor class
    def __init__(self, inventory = None): 
        if not inventory: 
            inventory = []
        self.inventory = inventory
    
    # add method 
    def add(self, item): 
        self.inventory.append(item)
        return item
    
    # remove method
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        
        return False
    
    # method that returns the name of the class
    def get_by_id(self, id): 
        for item in self.inventory: 
            if item.id == id: 
                return item
        
        return None