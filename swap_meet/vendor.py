# Defining class Vendor
class Vendor:
    # inventory is an empty list
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        if item:
            self.inventory.append(item)
            return item
        
    def remove(self, item):
        if item == item:
            self.inventory.remove(item)
            return item
