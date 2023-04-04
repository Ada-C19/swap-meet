from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        try:
            self.inventory.remove(my_item)
        except ValueError:
            return False
        try:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
        except ValueError:
            self.inventory.append(my_item)
            return False
        return True

