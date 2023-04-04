from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        # if this item in in inventory with matchind ID. return the item
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        # removes MY_ITEM from this Vendor then adds to friend
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
        # if len(self.inventory) or len(other_vendor.inventory) == 0:
            return False 
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        
