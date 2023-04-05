class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory  =  []
        else:
            self.inventory  = inventory
            
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
        
    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
        
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        else:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, my_item, their_item)
