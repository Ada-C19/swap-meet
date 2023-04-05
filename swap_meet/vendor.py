class Vendor:
    
    # constructor for the vendor class
    def __init__(self, inventory = None): 
        if not inventory: 
            inventory = []
        self.inventory = inventory
    
    # add method 
    def add(self, item): 
        self.inventory.append(item)
        return item
    
    # remove method
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        
        return False
    
    # method that returns the name of the class
    def get_by_id(self, id): 
        for item in self.inventory: 
            if item.id == id: 
                return item
        
        return None
    
    # method to swap items between two vendors
    def swap_items(self, other_vendor, my_item, their_item): 
        # both vendors need to have their respective items in order to swap
        if my_item in self.inventory and their_item in other_vendor.inventory: 
            self.remove(my_item)
            self.add(their_item)

            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        
        return False
    
    # method to swap first items between two vendors
    def swap_first_item(self, other_vendor): 
        if not self.inventory or not other_vendor.inventory: 
            return False    
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        self.remove(my_first_item)
        self.add(their_first_item)

        other_vendor.remove(their_first_item)
        other_vendor.add(my_first_item)

        return True
    
    # 