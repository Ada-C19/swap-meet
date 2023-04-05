class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
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
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
            if not self.inventory or not other_vendor.inventory:
                return False
        
            first_item = self.inventory[0]
            friends_first_item = other_vendor.inventory[0]

            other_vendor.inventory.append(first_item)
            self.inventory.append(friends_first_item)
            other_vendor.inventory.remove(friends_first_item)
            self.inventory.remove(first_item)
            return True
            

            


        
        


