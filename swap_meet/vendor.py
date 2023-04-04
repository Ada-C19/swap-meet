class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    

    def swap_first_item(self, other_vendor):
        """
        Swap the first items between self's inventory and other_vendor inventory.
        Return False if either inventory is empty.
        """
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_item = self.inventory[0]
        other_item = other_vendor.inventory[0]

        self.remove(my_item)
        other_vendor.remove(other_item)

        self.add(other_item)
        other_vendor.add(my_item)
        
        return True
    

    def get_by_category(self, category):
        """
        Return a list of items in inventory with category attribute that matches 
        the given category.
        """
        category_items = [item for item in self.inventory if item.category == category]
        return category_items


    def get_best_by_category(self, category):
        """
        Return item from inventory with highest condition score that matches given category.
        """
        max_condition = 0
        best_item = None
        
        for item in self.inventory:
           if item.category == category and item.condition > max_condition:
               best_item = item

        return best_item 
