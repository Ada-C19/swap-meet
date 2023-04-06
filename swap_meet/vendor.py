class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
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

    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False 
        
        if my_item in self.inventory or their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        