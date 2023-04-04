class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item = 'new item'):
        self.inventory.append(item)
        return item
    
    def remove(self, item = 'item to remove'):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self, id = int):
        for item in self.inventory:
            if item.id == id:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        else:
            other_vendor.remove(their_item)
            self.add(their_item)
            self.remove(my_item)
            other_vendor.add(my_item)
            
            return True

    def swap_first_item(self,other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        
        return True

