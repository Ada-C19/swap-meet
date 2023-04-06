class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        
        return item
    

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        
        return item
    

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None
    

    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        other_vendor.remove(their_item)
        self.remove(my_item)
        self.add(their_item)
        other_vendor.add(my_item)
        
        return True

    def swap_first_item(self, other_vendor):
        """
        Swap the first items between self's inventory and other_vendor inventory.
        Return False if either inventory is empty.
        """
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_item, their_item)
        
        return True


    def get_by_category(self, category):
        """
        Return a list of items in inventory with category attribute that matches 
        the given category.
        """
        category_items = [item for item in self.inventory if item.get_category() == category]
        
        return category_items


    def get_best_by_category(self, category):
        """
        Return item from inventory with highest condition score that matches 
        given category.
        """
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        best_item = max(category_items, key=lambda item: item.condition)

        return best_item 

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # Find item in self's inventory that matches other_vendor's priority
        my_item = self.get_best_by_category(their_priority)
        # Find item in other_vendor's inventory that matches my priority
        their_item = other_vendor.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False
        
        # Swap the two items
        self.swap_items(other_vendor, my_item, their_item)

        return True
    
    def get_newest(self):
        """
        Finds the first instance of newest item in an inventory.
        Returns False if inventory is empty, otherwise returns the newest item.
        """
        if not self.inventory: return False

        newest_item = min(self.inventory, key=lambda x:x.age)
        
        return newest_item
    
    def swap_by_newest(self, other_vendor):
        """
        Swaps the newest item from self and another vendor.
        Returns False if either inventory is empty, 
            otherwise mutates both inventories and returns True.
        """
        my_item = self.get_newest()
        their_item = other_vendor.get_newest()

        if not my_item or not their_item:
            return False
        
        self.swap_items(other_vendor, my_item, their_item)
        
        return True
        

