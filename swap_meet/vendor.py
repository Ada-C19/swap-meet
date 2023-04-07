class Vendor:
    def __init__(self, inventory = None):
        # If there is no inventory, set self.inventory to an empty list
        if inventory is None:
            self.inventory = []
        # if there is inventory, set it to the provided inventory
        else: 
            self.inventory = inventory
    def add(self, item):
        # Add the item to the inventory and return the item that was added
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        # try the item exists in the inventory, remove it and return the removed item, else raise error
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, id):
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        # Iterate through the inventory to find an item with a matching id
        for item in self.inventory:  
            # If an item with a matching id is found, return it  
            if item.id == id:
                return item
        # If no matching item is found, return None
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        # If either the `my_item` is not in this Vendor's inventory or the `their_item` 
        # is not in the other Vendor's inventory, return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        # Remove `my_item` from this Vendor's inventory and add it to the other Vendor's inventory
        self.remove(my_item)
        other_vendor.inventory.append(my_item)
        # Remove `their_item` from the other Vendor's inventory and add it to this Vendor's inventory
        other_vendor.inventory.remove(their_item)
        self.add(their_item)
        # If successful, return True
        return True
    
    # def swap_first_item(self, other_vendor):
    #     # Check if either the vendor or the friend have empty inventory, and return False if so
    #     if not self.inventory or not other_vendor.inventory:
    #         return False
    #     # Swap the first item from the friend's inventory with the first item from the vendor's inventory
    #     return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    def swap_first_item(self, other_vendor):
        try:
            # Check if either the vendor or the friend have empty inventory, and return False if so
            if not self.inventory or not other_vendor.inventory:
                return False
            # Swap the first item from the friend's inventory with the first item from the vendor's inventory
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        except IndexError:
            return False

    def get_by_category(self, category):
        # Create an empty list to store the matching items
        items_matching_category = []
        # Iterate through the inventory to find items with matching category
        for item in self.inventory:
            if item.get_category() == category:
                items_matching_category.append(item)
        # Return the list of matching items
        return items_matching_category


    def get_best_by_category(self, category):
        # Check if there are any items in the inventory with the given category
        if not self.get_by_category(category):
            # If there are no items in the inventory with the given category, return None
            return None
        # If there are items in the inventory with the given category, find the one with the highest condition
        return max(self.get_by_category(category), key=lambda item: item.condition)


    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # Check if the current vendor has an item of the category specified by their_priority
        # or if the other vendor has an item of the category specified by my_priority.
        if not self.get_best_by_category(their_priority) or not other_vendor.get_best_by_category(my_priority):
            # If either of these conditions is not met, return False as the swap cannot happen.
            return False
        
        # If both vendors have items to swap, call the swap_items method to swap the best items.
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        self.swap_items(other_vendor, my_item, their_item)
        return True
    def swap_by_newest(self, other_vendor):
        # Sort the inventory of both vendors by the age of the items
        my_inventory_sorted = sorted(self.inventory, key=lambda item: item.age)
        their_inventory_sorted = sorted(other_vendor.inventory, key=lambda item: item.age)
        # Find the newest item in each inventory
        my_newest_item = my_inventory_sorted[0] if my_inventory_sorted else None
        their_newest_item = their_inventory_sorted[0] if their_inventory_sorted else None

        # If either vendor does not have any items, return False
        if not my_newest_item or not their_newest_item:
            return False

        # Swap the newest items
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)