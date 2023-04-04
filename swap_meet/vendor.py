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
        #from vendor inventory remove my_item and add to other_vendor inventory
        #from other_vendor inventory remove their_item and add to vendor inventory
        #return True
        #if either vendor doesn't have item in inventory return False
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            return True
        elif their_item in other_vendor.inventory:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
        