class Vendor:
    def __init__(self, inventory=None):
        # If inventory is not None, it will be assigned to self.inventory
        # if inv IS None, then [] will be assigned to self.inventory
        self.inventory = inventory or []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
        return False 