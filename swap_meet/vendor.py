from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item 
    
    def get_by_id(self, id):
        for items in self.inventory:
            if items.id == id:
                return items
        return None
        

    def swap_items(self, other_vendor, my_item ,their_item):
        if my_item in self.inventory:
            if their_item in other_vendor.inventory:
                other_vendor.inventory.append(my_item)
                self.inventory.remove(my_item)
                self.inventory.append(their_item)
                other_vendor.inventory.remove(their_item)
            else:
                return None 
        
        
        return other_vendor.inventory and self.inventory
        
        #Conditional checking if their item in other vendor.inventory - add to inventory