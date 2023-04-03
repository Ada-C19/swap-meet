class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory # needs to be an empty list by default
    
    # adds single item to inventory and returns item added
    def add(self, item):  
        self.inventory.append(item)
        return item
    
    # removes single item from invetory, returns item removed | if not matching item in inventory, method should return False
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        return False
 

# instantiate a list and optionally pass in a list with keyword arg named inventory
# vendor_example = Vendor(inventory=[])   


    



