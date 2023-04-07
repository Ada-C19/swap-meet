from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
        
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            return True
        return False
        
    def swap_first_item(self, other_vendor):
        len_mine = len(self.inventory)
        len_their = len(other_vendor.inventory)

        if len_mine != 0 and len_their != 0:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True
        return False
        
    def get_by_category(self, category):
        of_category = []
        for item in self.inventory:
            if item.get_category() == category:
                of_category.append(item)
        return of_category
    
    def get_best_by_category(self, category):
        of_category = self.get_by_category(category)
        if len(of_category) == 0:
            return None
        best_of_category = max(of_category, key=lambda item: item.condition)
        return best_of_category
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        what_vendor_wants = self.get_best_by_category(their_priority)
        what_other_wants = other_vendor.get_best_by_category(my_priority)
        if what_vendor_wants is None or what_other_wants is None:
            return False
        self.swap_items(other_vendor, what_vendor_wants, what_other_wants)
        return True
    
    def swap_by_newest(self, other_vendor):
        len_mine = len(self.inventory)
        len_their = len(other_vendor.inventory)

        if len_mine != 0 and len_their != 0:
            my_newest = min(self.inventory, key=lambda item: item.age)
            their_newest = min(other_vendor.inventory, key=lambda item: item.age)
            self.swap_items(other_vendor, my_newest, their_newest)
            return True
        return False