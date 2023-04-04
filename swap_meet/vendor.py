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
    # from inventory
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    # This methods removes my_item from my inventory and adds it to my friend's inventory.
    # Returns True when removes and adds and False when my item is not in my inventory
    # And my friend's item is not in their inventory
    # Have to check if item is in INVENTORY first
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
    # Return True
    # If EITHER itself or friend = [] inventory Return False
    def swap_first_item(self, other_vendor):
        if other_vendor.inventory and self.inventory:
            first_item_from_friend = other_vendor.inventory[0]
            my_first_item = self.inventory[0]
            
            self.inventory[0] = first_item_from_friend
            other_vendor.inventory[0] = my_first_item
            return True
        return False

    # Returns a list of objects in Inventory with that category
    # Return [] if there are no items that matches
    def get_by_category(self, category):

        item_in_category = []
        for item in self.inventory:
            if category == item.get_category():
                item_in_category.append(item)
        return item_in_category




