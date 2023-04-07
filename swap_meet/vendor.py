class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        else: 
            removed_item = item
            self.inventory.remove(item)
            return removed_item

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
    
    def swap_items(self, other_vendor, my_item, their_item):
        if (not my_item in self.inventory 
            or not their_item in other_vendor.inventory):
            return False
        my_removed = self.remove(my_item)
        other_removed = other_vendor.remove(their_item)
        other_vendor.add(my_removed)
        self.add(other_removed)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        instance_item = self.inventory.pop(0)
        friends_item = other_vendor.inventory.pop(0)
        self.add(friends_item)
        other_vendor.add(instance_item)
        return True

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if items:
            return max(items, key=lambda item: item.condition)
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, best_item_for_them, best_item_for_me)
    
    def swap_by_newest(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_newest_item = min(self.inventory, key=lambda item: item.age)
            other_vendor_newest_item = min(other_vendor.inventory, key=lambda item: item.age)

            return self.swap_items(other_vendor, my_newest_item, other_vendor_newest_item)