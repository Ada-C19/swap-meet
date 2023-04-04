class Vendor:
    
    def __init__(self,inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory 

    def add (self, item):
        self.inventory.append(item)
        return item 
    
    def remove (self, item):
        try:  
            self.inventory.remove(item)
            return item 
        except ValueError: 
            return False 
    
    def get_by_id(self, integer): 
        for item in self.inventory: 
            if integer == item.id: 
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item): 
        if my_item in self.inventory and their_item in other_vendor.inventory:     
            self.remove(my_item)
            self.add(their_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            return True 
        return False 
    
    def swap_first_item(self, other_vendor):
        try: 
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory [0]
        except IndexError:
            return False 
        first_item_switch = self.swap_items(other_vendor, my_first_item, their_first_item)
        return first_item_switch 