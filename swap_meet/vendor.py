from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def swap_items(self, other_vendor, my_item, their_item ):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def get_by_id(self,id):
        for items in self.inventory:
            if items.id == id:
                return items
        return None
    
      
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory ) == 0 or len(other_vendor.inventory) == 0:
            return False 

        my_first_item = self.inventory[0]
        friends_first_item = other_vendor.inventory[0]
        self.remove(my_first_item)
        self.add(friends_first_item)
        other_vendor.remove(friends_first_item)
        other_vendor.add(my_first_item)
        return True

       


        
        
    