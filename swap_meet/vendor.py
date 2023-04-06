from .item import Item


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

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or
                their_item not in other_vendor.inventory):
            return False
      
        self.remove(my_item)
        other_vendor.add(my_item)
      
        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
     
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
 
        self.remove(my_first_item)
        other_vendor.add(my_first_item)
      
        other_vendor.remove(their_first_item)
        self.add(their_first_item)
      
        return True
  
    def get_by_category(self, category):
        category_items = [item for item in self.inventory
                          if item.get_category() == category]
  
        return category_items

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)

        if not category_items:
            return None

        best_item = max(category_items, key=lambda item: item.condition)

        return best_item


# - `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
#   - It takes in three arguments
#     - `other_vendor`, which represents another `Vendor` instance to trade with
#     - `my_priority`, which represents a category that the `Vendor` wants to receive
#     - `their_priority`, which represents a category that `other_vendor` wants to receive
#   - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other_vendor`'s inventory that matches `my_priority`
#     - It returns `True`
#     - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
#     - If `other_vendor` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.inventory.remove(my_best_item)
        other_vendor.inventory.remove(their_best_item)

        self.inventory.append(their_best_item)
        other_vendor.inventory.append(my_best_item)


        return True
