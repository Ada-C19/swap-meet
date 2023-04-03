class Vendor:
    # attribute -> inventory == []
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
    # method -> takes in item, adds item to inventoryattribute, returns item 
    def add(self, item): 
        self.inventory.append(item)
        return item
    # method -> takes in item, removes the matching item, returns item
    #        -> if no match, return False
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False