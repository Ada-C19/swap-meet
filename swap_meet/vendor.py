from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item): 
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

# - Instances of `Vendor` have an instance method named `get_by_id`
#   - This method takes one argument: an integer, representing an `Item`'s `id`
#   - This method returns the item with a matching `id` from the inventory
#   - If there is no matching item in the `inventory`, the method should explicitly return `None`
    def get_by_id(self, id_num):

        for item in self.inventory:
            if item.id and item.id == id_num:
                #return the value stored in the variable "item" 
                return item
        else:
            return None

