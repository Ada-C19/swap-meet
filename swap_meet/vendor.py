class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        try:
            for i in range(len(self.inventory)):
                if self.inventory[i].id == id:
                    return self.inventory[i]
        except:
            return None

    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False   
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True