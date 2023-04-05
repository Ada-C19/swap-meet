from swap_meet.item import Item

class Vendor:
    
    def __init__(self,inventory=[]):
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

        else:
            return None
        
    def swap_items(self,other_vendor,my_item,their_item):
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
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.inventory[0] = their_first_item
            other_vendor.inventory[0] = my_first_item
            return True        
        
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        best_item = None
        highest_condition = 0
        for item in items_in_category:
            if item.condition > highest_condition and item != best_item:
                highest_condition = item.condition
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = self.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)