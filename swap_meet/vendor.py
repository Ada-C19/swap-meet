class Vendor():
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        

    def add(self, item):        
        inventory = self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        inventory = self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        other_vendor.inventory
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.remove(their_item)
        self.inventory.append(their_item)

        return True




# remove my_item from vendor inventory and
# add item to other_vendor inventory

# remove their_item from the other_vendor inventory
# add their_item to to (our) vendor_inventory