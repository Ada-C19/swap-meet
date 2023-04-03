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
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        our_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]
        self.inventory[0] = friend_first_item
        other_vendor.inventory[0] = our_first_item
        return True
    def get_by_category(self,given_category):
        item_by_category = []
        for item in self.inventory:
            if item.category == given_category:
                item_by_category.append(item)
        return item_by_category
    def get_best_by_category(self, given_category):
        
        max_vale = -1
        for item in self.inventory:
            if item.category == given_category and item.condition > max_vale:
                best_item = item
                max_vale = item.condition
        if max_vale == -1:
            return None 
              
        return best_item


