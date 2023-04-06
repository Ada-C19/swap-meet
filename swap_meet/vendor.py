from swap_meet.item import Item

class Vendor:
    
    # constructor for the vendor class
    def __init__(self, inventory = None): 
        if not inventory: 
            inventory = []
        self.inventory = inventory
    
    # add method 
    def add(self, item): 
        self.inventory.append(item)
        return item
    
    # remove method
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        
        return False
    
    # method that returns the item based on id
    def get_by_id(self, id): 
        for item in self.inventory: 
            if item.id == id: 
                return item
        
        return None
    
    # method to swap items between two vendors
    def swap_items(self, other_vendor, my_item, their_item): 
        # both vendors need to have their respective items in order to swap
        if my_item in self.inventory and their_item in other_vendor.inventory: 
            self.remove(my_item)
            self.add(their_item)

            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        
        return False
    
    # method to swap first items between two vendors
    def swap_first_item(self, other_vendor): 
        if not self.inventory or not other_vendor.inventory: 
            return False    
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        self.remove(my_first_item)
        self.add(their_first_item)

        other_vendor.remove(their_first_item)
        other_vendor.add(my_first_item)

        return True
    
    
    def get_by_category(self, category):
        item_list = []
        
        for item in self.inventory: 
            if category == item.get_category(): 
                item_list.append(item)
        
        return item_list
    
    def get_best_by_category(self, category): 
        best_condition = 0
        best_item = None
        category_list = self.get_by_category(category)

        if not category_list: 
            return best_item
    
        for item in category_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item

        return best_item
        

    def swap_best_by_category(self, other_vendor, my_priority, their_priority): 
        # check to see if any of the inventories are empty. If one of them is, return False
        # (no swapping occurs)
        # obtain a list of items from each vendor based on the other vendors' priority (category)
            # if either list is empty, swapping cannot occur (return False)
            # else
                # obtain the best item from each list 
                # swap the items 
                # return true 
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None: 
            return False
        
        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True