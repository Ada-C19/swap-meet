class Vendor:
    def __init__(self, inventory = None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
   
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.add(their_item)
        self.remove(my_item)

        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        return True
    
    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        our_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, our_first_item, friend_first_item)
        return True
    
    def get_by_category(self,given_category):
        item_by_category = []
        for item in self.inventory:
            if item.category == given_category:
                item_by_category.append(item)
        return item_by_category
    
    
    def get_best_by_category(self, given_category):
        items_in_category_list = self.get_by_category(given_category)
        if not items_in_category_list:
            return None
        
        return max(items_in_category_list, key = lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item_thier_priority = self.get_best_by_category(their_priority)
        their_best_item_my_priority = other_vendor.get_best_by_category(my_priority)
        
        if not my_best_item_thier_priority or not their_best_item_my_priority:
            return False
        self.swap_items(other_vendor, my_best_item_thier_priority, their_best_item_my_priority)
        return True

    def get_newest_item(self):
        return min(self.inventory, key = lambda item: item.age)

    def swap_by_newest(self, other_vendor):        
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()

        self.swap_items(other_vendor, my_newest_item, their_newest_item)
        return True