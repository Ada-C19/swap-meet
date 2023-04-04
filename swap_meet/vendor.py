from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
            if inventory is None:
                inventory = []
            self.inventory = inventory

    # create instance method called add that takes in one item
    # add that item to inventory via the instance method and return item

    def add(self, item):
        self.inventory.append(item)
        return item

    # create instance method called remove that takes in one item
    # method removes the matching item from inventory
    # return item
    # if no matching item, return false

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    # create instance method called get_by_id
    # takes one argument: an integer that represents an Item's id
    # method returns item with matching id from inventory 
    # if no matching item in inventory, return None

    def get_by_id(self, id):
        
        for item in self.inventory:
            if id == item.id:
                return item
    
        return None
    
    # swap_items meth. takes 3 args: other_vendor, my_item, 
    # their_item (if not in their inventory return False)
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

    # remove items from each vendor's inventory
    # append swapped items to each other's inventory if 
    # items exist in their inventories & return True
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)

        return True
    
    # method swaps first item in inventory of both vendors w/ 
    # swap_items 
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
    # Returns True if the swap is successful, else False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)
    
    # method takes in category & returns item w/ highest condition 
    # score within that category in the vendor's inventory
    def get_best_by_category(self, category):
        best_item = None
        for item in self.get_by_category(category):
            if not best_item or item.condition > best_item.condition:
                best_item = item
        return best_item
    
    # method swaps best item (highest condition score) in given category 
    # between the two vendors using swap_items 
    # Return True if the swap is successful, else False
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, their_best_item) if my_best_item and their_best_item else False