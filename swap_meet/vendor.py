class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item_add):
        self.inventory.append(item_add)
        return item_add
    
    def remove(self, item_remove):
        if item_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_remove)
            return item_remove