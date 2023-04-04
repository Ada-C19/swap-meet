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
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        instance_item = self.inventory.pop(0)
        friends_item = other_vendor.inventory.pop(0)
        self.inventory.append(friends_item)
        other_vendor.inventory.append(instance_item)
        return True

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items