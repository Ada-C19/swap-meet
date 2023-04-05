
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
    def swap_first_item(self, other_vendor): #usar la función anterior?
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
    # --- Wave 6 -------------------------------
    def get_by_category(self, category):
        """This method takes one argument: a string, representing a category
        and returns a list of objects in the inventory with that category"""
        item_by_category = []
        for item in self.inventory:
            if category == item.get_category():
                item_by_category.append(item)
        return item_by_category
    
    def get_best_by_category(self, category):
        """will get the item with the best condition in a certain category"""
        item_by_category = self.get_by_category(category)
        if not item_by_category:
            return None
        best_item = item_by_category[0]
        for item in item_by_category:
            if item.condition > best_item.condition:
                best_item = item
        return best_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """ This method swaps the best item of certain categories with another Vendor"""
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        self.swap_items(other_vendor,my_best,their_best)
        return True
