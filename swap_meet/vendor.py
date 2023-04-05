class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []
    #add takes in one item and adds it to inventory
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item
    #remove takes in one item and removes the matching item
    def remove(self,item):
        self.item = item
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
            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True


    def swap_first_item(self, other_vendor):
            if not self.inventory or not other_vendor.inventory:
                return False
            
            v1_item = self.inventory[0]
            v2_item = other_vendor.inventory[0]
            
            self.inventory[0] = v2_item
            other_vendor.inventory[0] = v1_item
            
            return True

"""
Understanding
"swap_first_item" for instances of class named "Vendor". 
takes one argument which, another instance of Vendor 
instance = friend who vendor will swap items with.

Application
swap first item of inventory
call method with first item of friends inv
remove first item from inv
add to friends(vice versa)
if calling instance or friend instance has empty inv
return false
"""


