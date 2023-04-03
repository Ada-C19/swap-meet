from .item import Item

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
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            return True