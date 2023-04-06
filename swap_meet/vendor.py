from swap_meet import item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            return item
        else:
            return False
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False 
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
            
    def swap_items(self, my_item, other_vendor, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in other_vendor.inventory:
            return False 
        
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        
        return True

        