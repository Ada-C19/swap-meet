class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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
        
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        len_mine = len(self.inventory)
        len_their = len(other_vendor.inventory)

        if len_mine != 0 and len_their != 0:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True
        else:
            return False
