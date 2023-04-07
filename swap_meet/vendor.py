class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

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
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        # self.inventory.remove(my_item)
        # self.inventory.append(their_item)
        # other_vendor.inventory.remove(their_item)
        # other_vendor.inventory.append(my_item)
        # return True

        self.inventory.append(other_vendor.inventory.pop(other_vendor.inventory.index(their_item)))
        other_vendor.inventory.append(self.inventory.pop(self.inventory.index(my_item)))
        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        # other_vendor.inventory.append(self.inventory.pop(0))
        # self.inventory.append(other_vendor.inventory.pop(0))
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, string):
        current_stock = []
        for item in self.inventory:
            if string == item.get_category():
                current_stock.append(item)
        return current_stock

    def get_best_by_category(self, string):
        best_item = None
        highest_condition = 0
        for item in self.inventory:
            if item.condition > highest_condition and string == item.get_category():
                highest_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
            my_best_item = self.get_best_by_category(their_priority)
            their_best_item = other_vendor.get_best_by_category(my_priority)
            # if my_best_item and their_best_item:
            #     self.swap_items(other_vendor, my_best_item, their_best_item)
            #     return True
            # return False
    
            return self.swap_items(other_vendor, my_best_item, their_best_item)
