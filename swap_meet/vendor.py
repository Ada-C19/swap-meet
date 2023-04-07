class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            index_of_item = self.inventory.index(item)
            self.inventory.pop(index_of_item)
            return item
        return False
    
    # Returns the item with a matching id
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    # This methods removes my_item from my inventory and adds it to my friend's inventory.
    # Returns True when removes and adds and False when my item is not in my inventory
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            item_to_other_vendor = self.remove(my_item)
            other_vendor.add(item_to_other_vendor)

            item_from_other_vendor_to_me = other_vendor.remove(their_item)
            self.add(item_from_other_vendor_to_me)
            return True
        else:
            return False
        
    # If 1st item in friends's inventory and itself. Adds them to each inventory
    # Return True. If either itself or friend = [] inventory Return False.
    def swap_first_item(self, other_vendor):
        if other_vendor.inventory and self.inventory:
            first_item_from_friend = other_vendor.inventory[0]
            my_first_item = self.inventory[0]

            self.swap_items(other_vendor, my_first_item, first_item_from_friend)

            return True
        return False

    # Returns a list of objects in Inventory within that category
    # Return [] if there are no items that matches
    def get_by_category(self, category):

        item_in_category = []
        for item in self.inventory:
            if category == item.get_category():
                item_in_category.append(item)
        return item_in_category
    
    # Will get the item with best condition in its category
    def get_best_by_category(self, category):
        
        items_from_category = self.get_by_category(category)

        if not items_from_category:
            return None
        
        return max(items_from_category, key=lambda item: item.condition)

    # Return True IF my best item with category matches their best item with its category
    # Return False if there is no item that MATCHES either their priority or my priority
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        item_I_want = other_vendor.get_best_by_category(my_priority)
        item_other_want = self.get_best_by_category(their_priority)
                                                            
        return self.swap_items(other_vendor, item_other_want, item_I_want)
    
    # method will return the newest item from that category
    def get_newest_item_in_category(self, category):
        items_from_category = self.get_by_category(category)

        if not items_from_category:
            return None
        
        return min(items_from_category, key=lambda item: item.age)

    # Swap best by age will take 1 parg = category
    def swap_by_newest(self, other_vendor, their_category, my_category):

        item_I_want = other_vendor.get_newest_item_in_category(my_category)
        item_they_want = self.get_newest_item_in_category(their_category)

        return self.swap_items(other_vendor, item_they_want, item_I_want)



        
        






