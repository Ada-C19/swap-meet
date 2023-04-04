class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            item_to_swap = self.inventory.pop(0)
            other_item_to_swap = other_vendor.inventory.pop(0)
            self.inventory.append(other_item_to_swap)
            other_vendor.inventory.append(item_to_swap)
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
        return None

    def get_newest_by_category(self, category):
        items = self.get_by_category(category)
        if items:
            return min(items, key=lambda item: item.age)
        return None
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        else:
            return self.swap_items(other_vendor, my_best_item, their_best_item)

######################################################################
############ OPTIONAL ENHANCEMENT ####################################
######################################################################


    def get_newest_by_category(self, category):
        items = self.get_by_category(category)
        if items:
            return min(items, key=lambda item: item.age)
        return None
    
    def swap_by_newest(self, other_vendor, my_priority, their_priority):
        my_newest_item = self.get_newest_by_category(their_priority)
        their_newest_item = other_vendor.get_newest_by_category(my_priority)

        if my_newest_item is None or their_newest_item is None:
            return False
        else:
            return self.swap_items(other_vendor, my_newest_item, their_newest_item)
