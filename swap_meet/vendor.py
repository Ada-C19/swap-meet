
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
           inventory = []
        self.inventory = inventory

    
    def add(self, item):
        """adds item to the inventory"""
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """removes the matching item from the inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    # ----- Wave 2 -----------------------------

    def get_by_id(self, id):
        """returns the item with matching id from inventory"""
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    # ----- Wave 3 -----------------------------

    def swap_items(self, other_vendor, my_item, their_item):
        """The method removes my_item from this Vendor's inventory, 
        and adds it to the friend's inventory
        Removes their_item from the other Vendor's inventory, 
        and adds it to this Vendor's inventory"""
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True    
    
    # ----- Wave 4 -----------------------------
    def swap_first_item(self, other_vendor):
        """This method considers the first item in the instance's inventory, 
        and the first item in the friend's inventory
        It removes the first item from its inventory, and adds the friend's first item
        It removes the first item from the friend's inventory, and adds the instances first item"""
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        self_first_element = self.inventory.pop(0)
        other_first_element = other_vendor.inventory.pop(0)
        self.inventory.append(other_first_element)
        other_vendor.inventory.append(self_first_element)
        return True
 
        
    
