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

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        for my_item in self.inventory and their_item in other_vendor.inventoryswasw:
            if len(my_item) == len(their_item):
                other_vendor.append(my_item)
                self.inventory.remove(my_item)
                self.inventory.append(their_item)
                other_vendor.remove(their_item)
        return True
            