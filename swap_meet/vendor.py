from .item import Item

class Vendor:
    # Define attributes for Vendor instances
    def __init__(self, inventory = None):
        # If no value provided for inventory, attribute inventory takes on an empty list 
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item_add):
        # Add item provided to attribute inventory
        self.inventory.append(item_add)
        # Return this added item
        return item_add
    
    def remove(self, item_remove):
        # If item to be removed doesn't exist in attribute inventory, return False.
        # Otherwise, remove this item from inventory and return this removed item
        if item_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_remove)
            return item_remove
        
    def get_by_id(self, id):
        # Create an Item instance passing in an id value
        test_item = Item(id)
        # Loop through list of instances stored in attribute inventory
        for item in self.inventory:
            # If attribute id in an instance has same value as attribute id in Item instance
            # Return this instance. Otherwise, return None
            if item.id == test_item.id:
                return item
        return None

            
    def swap_items(self, other_vendor, my_item, their_item):
        # If user's Item instance doesn't exist in own inventory or friend's Item instance doesn't exist
        # in friend's inventory, return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        # Otherwise, remove user's Item instance and add it to friend's inventory
        # Remove friend's Item instance and add it to user's inventory
        # Return True
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item(self, other_vendor):
        # If user's own inventory or friend's inventory is empty, return False
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            # Otherwise, grab first Item instance in user's and friend's inventories
            user_first_item = self.inventory[0]
            friend_first_item = other_vendor.inventory[0]
            # Call on the swap_items method to swap these first Item instances between user and friend
            self.swap_items(other_vendor, user_first_item, friend_first_item)
            # self.inventory.remove(user_first_item)
            # other_vendor.inventory.remove(friend_first_item)
            # other_vendor.inventory.append(user_first_item)
            # self.inventory.append(friend_first_item)
            return True
        
    def get_by_category(self, category):
        # Note: category of type string
        # Create an empty list called "resulting_list"
        resulting_list = []
        # Loop through each Item instance in inventory
        for item in self.inventory:
            # If an instance's category (aka class name) same as provided category,
            # add this instance to resulting_list
            if item.get_category() == category:
                resulting_list.append(item)
        # Return updated resulting_list
        return resulting_list
    
    def get_best_by_category(self, category):
        # Call on get_by_category method to get a list of instances matching provided category
        resulting_list = self.get_by_category(category)
        # If resulting_list is empty, aka no matching instances, return None
        if len(resulting_list) == 0:
            return None
        else:
            # Otherwise, grab first instance in resulting_list and store in best_item
            best_item = resulting_list[0]
            # Read first instance's attribute condition and store in best_condition
            best_condition = resulting_list[0].condition
            # Loop thru each instance in resulting_list
            for item in resulting_list:
                # If an instance's attribute condition shares same value as best_condition's value
                # re-assign this instance to best_item and its attribute condition to best_condition
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition
            # Return updated instance with best condition matching provided category
            return best_item    
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # Call on get_best_by_category method to get user's best instance matching friend's category
        # and to get friend's best instance matching user's category
        user_best_match = self.get_best_by_category(their_priority)
        other_best_match = other_vendor.get_best_by_category(my_priority)
        # If user has no instance matching friend's category or vice versa, return False
        if user_best_match is None or other_best_match is None:
            return False
        else: 
            # Otherwise, call on swap_items method to swap user's and friend's 
            # matching best instances with each other 
            self.swap_items(other_vendor, user_best_match, other_best_match)
            # return True
            return True