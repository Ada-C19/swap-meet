

class Vendor:
    # here a new instance of Vendor can either have a list or None option as a value for inventory
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item
