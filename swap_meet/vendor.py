from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    
    def swap_items(self, other_vendor, my_item, their_item):

        # verify each item is in their corresponding inventory
        # else return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # remove my_item from our own inventory and add to the other vendor's inventory
        self.remove(my_item)
        other_vendor.add(my_item)

        # remove their_item from other vendor's inventory and add to ours
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

