from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if not other_vendor.inventory or not self.inventory:
            return False
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, first_item, other_vendor_first_item)        
        return True

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, category):
        highest_item = None
        highest_rating = 0
        item_list = self.get_by_category(category)
        for item in item_list:
            if item.condition > highest_rating:
                highest_item = item
                highest_rating = item.condition
        return highest_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_we_want = other_vendor.get_best_by_category(my_priority)
        item_other_vendor_wants  = self.get_best_by_category(their_priority)
    
        if not item_other_vendor_wants or not item_we_want:
            return False
        self.swap_items(other_vendor, item_other_vendor_wants, item_we_want)
        return True 