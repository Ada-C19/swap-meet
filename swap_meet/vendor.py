class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def remove(self, item):
        if not self.inventory or item not in self.inventory:
            return False
        return item