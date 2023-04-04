class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        # Checks corresponding items are in inventories
        if (my_item not in self.inventory or 
                their_item not in other_vendor.inventory):
            return False
        
        # Gives vendor's item to other vendor
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)

        # Receives other vendor's item
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.inventory.append(other_vendor.inventory.pop(0))
        other_vendor.inventory.append(self.inventory.pop(0))

        return True