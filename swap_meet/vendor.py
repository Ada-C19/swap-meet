class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, object_id):
        for item in self.inventory:
            if item.id == object_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or\
        their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)    
        return True
            
    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        
        self.swap_items(other_vendor, self.inventory[0], \
        other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
        
    
    def get_best_by_category(self, category):
        return max(self.get_by_category(category), key=lambda item: item.condition, default=None)


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_from_me = self.get_best_by_category(their_priority)
        item_from_them = other_vendor.get_best_by_category(my_priority)

        if item_from_me and item_from_them:
            self.swap_items(other_vendor, item_from_me, item_from_them)
            return True
        else:
            return False

    def get_newest(self):
        return min(self.inventory, key= lambda item: item.age, default=None)

    def swap_by_newest(self, other_vendor):
        item_from_me = self.get_newest()
        item_from_them = other_vendor.get_newest()

        if item_from_me and item_from_them:
            self.swap_items(other_vendor, item_from_me, item_from_them)
            return True
        else:
            return False