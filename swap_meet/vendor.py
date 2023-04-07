class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory


    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item


    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        return False
    

    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None


    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False
    

    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
    
            first_item_swap = self.swap_items(other_vendor, my_item, their_item)
            # self.remove(my_item)
            # other_vendor.remove(their_item)
            # self.add(their_item)
            # other_vendor.add(my_item)
            return first_item_swap
        return False


    def get_by_category(self, category):
        item_list= []
        for item in self.inventory:
            if category == item.get_category():
                item_list.append(item)
        return item_list
        
        # use list comprehension
        # return [item for item in self.inventory if category == item.get_category()]
        
    
    def get_best_by_category(self, category):
        category_item = self.get_by_category(category)
        if not category_item:
            return None
        return max(category_item, key = lambda item:item.condition)
        
            
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        # if my_best_item is None or their_best_item is None:
        #     return False
        return self.swap_items(other_vendor, my_best_item, their_best_item)

