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
        if my_item in self.inventory and their_item in other_vendor.inventory: 
            self.remove(my_item)
            self.add(their_item)

            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        
        return False
    
    # method to swap first items between two vendors
    def swap_first_item(self, other_vendor): 
        try:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
        
        except IndexError:
            return False

        return self.swap_items(other_vendor, my_first_item, their_first_item)
    
    # method to retrieve all items in a particular category
    def get_by_category(self, category):
        item_list = []
        
        for item in self.inventory: 
            if item.get_category() == category: 
                item_list.append(item)
        
        return item_list
    
    # method to retrieve best condition item in a particular category
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
        
    # method to swap the best item (best condition) with another vendor so long
    # as both vendors have the type of items the other is looking for
    def swap_best_by_category(self, other_vendor, my_priority, their_priority): 
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None: 
            return False
        
        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True