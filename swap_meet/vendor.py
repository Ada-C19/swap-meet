class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item) # This method adds the item to the inventory
        return item
    
    def remove(self, item):
        if item not in self.inventory: # If there is no matching item in the inventory, the method should return False
            return False 
        
        self.inventory.remove(item) # This method removes the matching item from the inventory
        return item

    def get_by_id(self, id):
        for item in self.inventory: # Loops through each item in inventory
            if id == item.id: # Checks for id
                return item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        
        if self.inventory == [] or other_vendor.inventory == []: # Check for empty inventory for user or other vendor
            return False
        
        elif my_item not in other_vendor.inventory and their_item not in self.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True

    # Instances of Vendor have an instance method named swap_first_item
    # It takes one argument: an instance of another Vendor (other_vendor), 
    # representing the friend that the vendor is swapping with
    def swap_first_item(self, other_vendor):

        if self.inventory == [] or other_vendor.inventory == []: #  Check for empty inventory for user or other vendor
            return False
        
        # Helper variables
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
                
        if their_first_item not in self.inventory: # Checks for other vendor's item in inventory and swaps specified items
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.__class__.__name__ == category] # Appending items to list that match the same Class name
        return items

    def get_best_by_category(self, category):
        items = self.get_by_category(category) # Uses get_by_category function to find list of all items in that Class
        
        if not items: # Check for empty list
            return None
        
        return max(items, key= lambda item: item.condition) # Returns best condition within items in the specified Class


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        # Helper Variables
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if my_best_item is None or their_best_item is None: # Check for if priority items available
            return False
        
        self.swap_items(other_vendor, my_best_item, their_best_item) # Use swap_items function to swap requested items
        return True
