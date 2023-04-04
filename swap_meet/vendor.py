class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            # Remove my_item from this Vendor's inventory 
            item_to_friend = self.remove(my_item)
            # Add it to the friend's inventory
            other_vendor.add(item_to_friend)
            # Remove their_item from other Vendor's inventory
            item_to_me = other_vendor.remove(their_item)
            # add it to this Vendor's inventory
            self.add(item_to_me)
            return True
        # If item isn't in the inventory
        return False
    
    def swap_first_item(self, other_vendor):
        
        if other_vendor.inventory and self.inventory:
            my_first_item = self.inventory[0]
            friends_first_item = other_vendor.inventory[0]
            
            return self.swap_items(other_vendor, my_first_item, friends_first_item)
        
        return False
    
    def get_by_category(self, category):
        """Returns a list of objects in inventory with that category. 
        If no items in inventory match the category, returns an empty list.
        """
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        
        return category_list

        
    def get_best_by_category(self, category):
        """Returns the item with the highest condition and matching category. 
        Returns None if no items match.
        """

        highest_condition = 0

        category_list = self.get_by_category(category)
        for item in category_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
        
        for item in category_list:
            if item.condition == highest_condition:
                return item

        return None


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """Swaps the best item of certain category with another vendor. 
        Returns True, False if there are no matches.
        """
        
        their_item = other_vendor.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        
        return self.swap_items(other_vendor, my_item, their_item)
        


