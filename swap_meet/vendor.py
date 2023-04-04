class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, object_id):
        for item in self.inventory:
            if item.id == object_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or\
        their_item not in other_vendor.inventory:
            return False
        
        # remove my_item from this Vendor
        self.remove(my_item)
        # add my item to friend's inventory
        other_vendor.add(my_item)
        # remove their item from that Vendor
        other_vendor.remove(their_item)
        # add their item to my inventory
        self.add(their_item)    
        return True
            
        # if either item not in inventory
        # return False 