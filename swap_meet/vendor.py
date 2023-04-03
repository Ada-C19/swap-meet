class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            removed_item = item
            self.inventory.remove(item)
            return removed_item
        else:
            return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
    
    def swap_items(self, other_vendor, my_item, their_item):
        if (not my_item in self.inventory 
            or not their_item in other_vendor.inventory):
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        return True