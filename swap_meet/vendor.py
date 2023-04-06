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
        self_item = self.inventory[0]
        vendor_item = other_vendor.inventory[0]

        self.inventory.remove(self_item)
        self.inventory.append(vendor_item)

        other_vendor.inventory.remove(vendor_item)
        other_vendor.inventory.append(self_item)
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
     

        # my_best = self.get_best_by_category(their_priority)
        # their_best = other_vendor.get_best_by_category(my_priority)

        # if not my_best or not their_best:
        #     return False
        
        # self.swap_items(other_vendor, my_best, their_best)
        # return True
    
        # # def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # best_in_my = other_vendor.get_best_by_category(my_priority)
        # best_in_theirs  = self.get_best_by_category(their_priority)

        # if not best_in_theirs or not best_in_my or best_in_my != best_in_theirs:
        #     return False
        # self.swap_items(other_vendor, best_in_my, best_in_theirs)
        # return True 
        
        v_wants = other_vendor.get_best_by_category(my_priority)
        ov_wants  = self.get_best_by_category(their_priority)
        # if not ov_wants or not v_wants or v_wants != ov_wants:
    
        if not ov_wants or not v_wants:
            return False
        self.swap_items(other_vendor, ov_wants, v_wants)
        return True 