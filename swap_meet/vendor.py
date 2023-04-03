class Vendor:
    ### Wave 1

# In Wave 1 we will create the `Vendor` class.

# - There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
# - Inside this module, there is a class named `Vendor`
# - Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
# - When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`


# - Every instance of `Vendor` has an instance method named `add`, which takes in one item
# - This method adds the item to the `inventory`
# - This method returns the item that was added

# - Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
# - This method removes the matching item from the `inventory`
# - This method returns the item that was removed
# - If there is no matching item in the `inventory`, the method should return `False`

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

        # self.inventory = inventory 

        # inventory = inventory if inventory is not None else []
        # self.inventory = inventory 

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
    # - Instances of `Vendor` have an instance method named `get_by_id`
#   - This method takes one argument: an integer, representing an `Item`'s `id`
#   - This method returns the item with a matching `id` from the inventory
#   - If there is no matching item in the `inventory`, the method should explicitly return `None`

# print()
# inventory_list = ["a","b","c"]
# test_item = Vendor(inventory_list)
