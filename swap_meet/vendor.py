class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id):
# 7. Inside the Vendor class, define a method: get_by_id that takes one argument: an integer representing an Item's id.
# 8. Inside the get_by_id method, search the Vendor's inventory for an item with a matching id.
# 9. If there is a matching item, return that item.
# 10. If there is no matching item, return None