class Vendor:
    def __init__(self, inventory=None):
        # Initialize a Vendor instance with an empty inventory list
        # or with a provided inventory list
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
        
        # Add an item to the inventory list and return the item
    def add(self, item):
        self.inventory.append(item)
        return item
        
        # Remove an item from the inventory list if it exists and return the item
        # Otherwise, return False if the item is not found in the inventory list
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
