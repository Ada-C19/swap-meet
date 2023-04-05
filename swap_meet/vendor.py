class Vendor:
    def __init__(self, inventory=None):
        # If inventory is not None, whatever 'inventory' is passed in will be assigned to self.inventory
        # if inv IS None, then [] will be assigned to self.inventory
        self.inventory = inventory or []
    
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
            # python doesnt know .id exists but it is still going to try it
            # we do not need to import bc we're not inheriting anything
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # remove my_item from this Vendor's inv
        self.remove(my_item)
        # add this to friends inv
        other_vendor.add(my_item)
        # remove their_item from the other Vendors inv
        other_vendor.remove(their_item)
        # add this to vendor's inv
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor,my_first_item, their_first_item)

        return True
    
    def get_by_category(self):
        pass