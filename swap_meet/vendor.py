class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item = 'new item'):
        self.inventory.append(item)
        return item
    
    def remove(self, item = 'item to remove'):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self, id = int):
        for item in self.inventory:
            if item.id == id:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        else:
            self.inventory = self.inventory
            other_vendor.inventory = other_vendor.inventory
            other_vendor.remove(my_item)
            self.add(my_item)
            self.remove(their_item)
            other_vendor.add(their_item)
            
            return True



# print()
# inventory_list = ["a","b","c"]
# test_item = Vendor(inventory_list)

# Instances of `Vendor` have an instance method named `swap_items`
#   - It takes 3 arguments:
#   - `swap_items` takes 3 arguments:
#     1. an instance of another `Vendor` (`other_vendor`), representing the friend that the vendor is swapping with
#     2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
#     3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
#   - The method removes `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
#   - The method removes `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
#   - The method returns `True`
#   - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`
