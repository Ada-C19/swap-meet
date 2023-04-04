class Vendor:

    def __init__(self, inventory=None): # inventory = empty list. Optionally pass in Keyword argument inventory?
        if inventory is None: 
            inventory = []
        self.inventory = inventory

    def add(self, item):
        #  adds the item to the inventory
        self.inventory.append(item)
        # returns the item that was added
        return item
    
    def remove(self, item):
        # method removes the matching item from the inventory
        if item in self.inventory: 
            self.inventory.remove(item)
        # returns the item that was removed
            return item 
        #If there is no matching item in the inventory, the method should return False
        return False 
    
    def get_by_id(self, id):
        for item in self.inventory:
            #return the item with a matching if from the inventory
            if item.id == id:
                return item
        return None