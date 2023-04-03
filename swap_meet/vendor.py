from swap_meet.item import *

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
        # self.id = Item(self.id)

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        pass
        


    """- Instances of `Vendor` have an instance method named `get_by_id`
  - This method takes one argument: an integer, representing an `Item`'s `id`
  - This method returns the item with a matching `id` from the inventory
  - If there is no matching item in the `inventory`, the method should explicitly return `None`"""