class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            item_for_friend = self.remove(my_item)
            other_vendor.add(item_for_friend)
            
            item_for_me = other_vendor.remove(their_item)
            self.add(item_for_me)
            return True
    
        return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)


    def get_by_category(self, category):
        category_list = []  
        
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        
        return category_list
    
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None
        
        best_condition = 0
        best_item = None

        for item in category_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item

        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item == None or their_best_item == None:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)
        


        





