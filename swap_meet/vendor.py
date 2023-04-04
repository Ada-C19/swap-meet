class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_item = self.inventory[0]
        print("my_item:", my_item)
        other_item = other_vendor.inventory[0]

        self.remove(my_item)
        print("after remove, self inventory:", self.inventory)
        other_vendor.remove(other_item)
        

        self.add(other_item)
        other_vendor.add(my_item)
        return True