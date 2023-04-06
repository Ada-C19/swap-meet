from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else []

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
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, my_item = self.inventory[0] , their_item = other_vendor.inventory[0])
        
        return True
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list
        
    

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

    def swap_by_newest(self,other_vendor):
        my_newest_item = min(self.inventory, key= lambda item: item.age, default=None)
        their_newest_item = min(other_vendor.inventory, key=lambda item: item.age, default=None)

        if my_newest_item and their_newest_item:
            return self.swap_items(other_vendor, my_newest_item, their_newest_item)
        
        else:
            return False