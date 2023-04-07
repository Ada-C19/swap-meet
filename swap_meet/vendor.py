class Vendor:
    """
    A class that represents Vendor.
    Each Vendor has an attribute named inventory, which is an empty list by default.
    """
    def __init__(self, inventory=None): 
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        """
        Add item to inventory, return item
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Remove the matching item in the inventory, return the item.
        If no matching item, return False.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_id(self, id):
        """
        Return the irem with a matching id from the inventory.
        If no matching item return None.
        
        Args:
            id (integer): Item's id.
        """
        for item in self.inventory:
            if id == item.id:           
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swap this Vendor's item with the other Vendor's item, return Ture.
        If either Vendor does not have a matching item, return False.

        Args:
            other_vendor (an instance of Vendor)
            my_item (an instance of Item): representing the item this Vendor instance plans to give.
            their_item (an instence of Item): representing the item the other Vendor plans to give.
        """
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, other_vendor):
        """
        Swap the first item in this Vendor with the first irem in the other Vendor, return True.
        If either Vendor does not have a matching item, return False.
        """
        if not self.inventory or not other_vendor.inventory: 
            return False
        else:
            my_first = self.inventory[0]
            their_first = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_first, their_first)
            return True
        
    def get_by_category(self, category):
        """
        Returns a list of objects in the inventory with that category.
        If no matching item, return empty list.
        
        Args:
            category (string): representing a category.
        """
        category_items = []
        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)
        return category_items
        
    def get_best_by_category(self, category):
        """
        Return the item with the best condition in a certain category.
        If no matching item, return None.
        
        Args:
            category (string): representing a category.
        """
        if not self.get_by_category(category):
            return None
        else:
            return max(self.get_by_category(category), key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swap the best item in this Vendor that matches their_priority category with the best item in the other Vendor that matches my_priority, return True.
        If either Vendor has no matching item, return False.

        Args:
            other_vendor (an instence of Vendor): _description_
            my_priority (string): epresents a category that this Vendor wants to receive.
            their_priority (string): epresents a category that the other Vendor wants to receive.
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other_vendor, my_item, their_item)
            return True