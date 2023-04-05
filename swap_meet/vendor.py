from swap_meet.item import Item
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

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):    
        #yaels: if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
        #both work!
        if not self.inventory or not other_vendor.inventory:
            return False
        other_vendor.inventory.append(self.inventory.pop(0))
        self.inventory.append(other_vendor.inventory.pop(0))
        return True
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
        
        # category_list = []
        # for item in self.inventory:
        #     if isinstance(item, category):
        #         category_list.append(item)
        # return category_list

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        best_item = None
        best_condition = -1.0
        for item in items:
            if item.condition > best_condition:
                best_item = item 
                best_condition = item.condition
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        else: 
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True

        
    
