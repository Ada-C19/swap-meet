class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        instance_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, instance_first_item, other_vendor_first_item)

        return True