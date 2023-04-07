class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id: 
                return item
        return None

    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False 
        
        if my_item in self.inventory or their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False
        else:
            # Called method swap_items and used indexing to make sure first items are swapped
            self.swap_items( other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        
    def get_by_category(self,category):
        category_list = []

        for item in self.inventory:
            # Called component method to get a category for comparison in conditional
            if category == item.get_category():
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, category):

        best_item = None
        for item in self.get_by_category(category):
            # Used component attribute for comparisons
            if best_item == None or item.condition > best_item.condition:
                best_item = item 
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        # Called another method to get the best as priority items
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        # Both need to be true in order to swap items
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        return False
        

                

        
                
            
