from uuid import uuid4

class Item:
    def __init__(self, id=None):
        self.id = uuid4().int if id is None else id
    # use this in wave 5 (probably for all modules)

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        # check if need to cast into str
        pass
    

    # def swap_first_item(self, other_vendor):
    #     """
    #     Swap the first items between self's inventory and other_vendor inventory.
    #     Return False if either inventory is empty.
    #     """
    #     if not self.inventory or not other_vendor.inventory:
    #         return False
        
    #     my_item = self.inventory[0]
    #     other_item = other_vendor.inventory[0]

    #     self.remove(my_item)
    #     other_vendor.remove(other_item)

    #     self.add(other_item)
    #     other_vendor.add(my_item)
        
    #     return True