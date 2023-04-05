class Vendor:

    def __init__(self, inventory = None):
        if inventory == None: 
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

        return False
    
    def get_by_id(self, input_id):
        for item in self.inventory:
            if item.id == input_id:
                return item 
        
        return None 
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False 

        self.remove(my_item)
        other_vendor.add(my_item)
                
        self.add(their_item)
        other_vendor.remove(their_item)

        return True    
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
        
    
    def get_by_category(self, category):
        inventory_list = []
        for item in self.inventory:
            if item.get_category() == category:
                inventory_list.append(item)

        return inventory_list 

    def get_best_by_category(self, category):
        max_condition = 0 
        best_item = None
        for item in self.inventory:
            if item.get_category() == category and item.condition > max_condition:
                max_condition = item.condition 
                best_item = item 
        
        return best_item 
                

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_item_for_swap = self.get_best_by_category(their_priority)
        their_item_for_swap = other_vendor.get_best_by_category(my_priority)
        
        if my_item_for_swap is None or their_item_for_swap is None:
            return False 
        else:
            return self.swap_items(other_vendor, my_item_for_swap, their_item_for_swap)