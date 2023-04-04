class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory 
        #add takes in one item and adds it to inventory
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item
    #remove takes in one item and removes the matching item
    def remove(self,item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
            
