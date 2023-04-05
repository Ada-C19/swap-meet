from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item 

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return 
    
    def swap_items(self, other_vendor, my_item, their_item):
        ''' Swap items between two vendors and their inventories'''
        
        # check items exist in own vendor and other vendor
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        # swap my_item into other_vendor inventory
        other_vendor.add(my_item)
        self.remove(my_item)

        # swap their_item into self inventory
        self.add(their_item)
        other_vendor.remove(their_item)
        return True
            