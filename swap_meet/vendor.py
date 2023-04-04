from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None): 
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.name = "Vendor"
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False 
        
        self.inventory.remove(item)
        return item

    def get_by_id(self, current_id):
        # item_id = Item().id
        for item in self.inventory:
            if current_id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        other_vendor_inventory = other_vendor.inventory
        current_vendor_inventory = self.inventory
        if my_item not in current_vendor_inventory or their_item not in other_vendor_inventory:
            return False
        
        current_vendor_inventory.remove(my_item)
        other_vendor_inventory.append(my_item)
        other_vendor_inventory.remove(their_item)
        current_vendor_inventory.append(their_item)
        return True

