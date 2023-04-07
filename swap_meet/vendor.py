class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item

    def remove(self,item):
        self.item = item
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
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True

    def swap_first_item(self, other_vendor):
            if not self.inventory or not other_vendor.inventory:
                return False
            
            v1_item = self.inventory[0]
            v2_item = other_vendor.inventory[0]
            
            self.inventory[0] = v2_item
            other_vendor.inventory[0] = v1_item
            
            return True

    def get_by_category(self, category):
        
        matching_items = []

        for item in self.inventory:
            if item.get_category() == category:
                matching_items.append(item)
            if not matching_items:
                return None
        return matching_items

        
    def get_best_by_category(self, category):

        matching_items = [item for item in self.inventory if item.category == category]
        if not matching_items:
            return None
        return max(matching_items, key=lambda item: item.condition)
        

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False

        self.inventory.remove(my_best_item)
        other_vendor.inventory.remove(their_best_item)
        self.inventory.append(their_best_item)
        other_vendor.inventory.append(my_best_item)

        return True