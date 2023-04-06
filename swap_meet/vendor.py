from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)

        return item
    
    def remove(self, item):
        self.item = item
        
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self,id):
        
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        self.inventory.append(their_item)

        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)

        return True
