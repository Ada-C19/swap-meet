class Vendor:
    def __init__(self, inventory=None):
        self.inventory = self.empty_list_creator(inventory)

    def empty_list_creator(self, inventory):
        self.inventory = [] if inventory is None else inventory
        return self.inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for thing in self.inventory:
            if item == thing:
                self.inventory.remove(thing)
                return item
        return False