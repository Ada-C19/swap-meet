class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if not self.inventory:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, other_vendor_first_item)
        return True

    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category):
        options = self.get_by_category(category)
        if options:
            best_condition_avail = max(option.condition for option in options)
        else:
            return None
        for option in options:
            if option.condition == best_condition_avail:
                return option
            
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_other_vendor_wants = self.get_best_by_category(their_priority)
        item_self_wants = other_vendor.get_best_by_category(my_priority)
        if item_other_vendor_wants and item_self_wants:
            self.swap_items(other_vendor, item_other_vendor_wants, item_self_wants)
            return True
        else:
            return False
            