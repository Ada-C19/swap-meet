# vendor class attributes
# init methos (self)
# -keyword arg (optional) inventory(empty list)
# add method (return item added to list)
# remove method (return item removed from list)
# if no matching item found return False
class Vendor:
    # passing optional argument called inventory 
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    # method that adds item to inventory 
    def add(self, item):
        if item:
            self.inventory.append(item)
        return item 
    # method that removes item from inventory if in inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item 