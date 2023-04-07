from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self, added_item):
        (self.inventory).append(added_item)
        return added_item
    
    def remove(self,item_removed):
        if item_removed not in self.inventory:
            return False
        else:
            for item in self.inventory:
                if item_removed == item:
                    (self.inventory).remove(item)
                    return item_removed

    def get_by_id(self, id_num):
        for item in self.inventory:
            if item.id == id_num:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        
    def get_by_category(self, category_type):
        items_in_category = []
        for item in self.inventory:
            if category_type == item.get_category():
                items_in_category.append(item)
        return items_in_category
        
    def get_best_by_category(self,category):
        if not self.get_by_category(category):
            return None
        else:
            items_by_category = self.get_by_category(category)
            best_condition = max(items_by_category, key=lambda items: items.condition)
            return best_condition
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_best_item = other_vendor.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)
        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True