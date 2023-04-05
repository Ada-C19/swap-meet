

class Vendor:
    #
    def __init__(self, inventory=None):
        # if inventory is truthy, values will be assigned to inventory
        if inventory:
            self.inventory = inventory
            # otherwise, []
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item
