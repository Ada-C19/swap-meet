class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

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
        for item in self.invetory:
            if item.id == id:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in self.inventory:
            if my_item not in other_vendor.inventory:
                self.inventory.remove(my_item)
                other_vendor.inventory.remove(their_item)
                self.inventory.append(their_item)
                other_vendor.inventory.append(my_item)
                return True
        return False 
        
        
