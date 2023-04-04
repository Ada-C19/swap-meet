class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)

        return item
    
    def remove(self, matching_item):
        self.item = matching_item
        
        if matching_item in self.inventory:
            self.inventory.remove(matching_item)
            return matching_item
        else:
            return False
