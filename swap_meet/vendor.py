

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

# if theres a match, item gets removed
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        else:
            return False
