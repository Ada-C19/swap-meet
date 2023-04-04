from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
           inventory = []
        self.inventory = inventory

    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    def get_by_id(self, id):
        # returns the item with matching id from inventory
        for element in self.inventory:
            if element.id == id:
                return element
            return None
    def swap_items(self, other_vendor, my_item, their_item):
        """The method removes my_item from this Vendor's inventory, 
        and adds it to the friend's inventory
        The method removes their_item from the other Vendor's inventory, 
        and adds it to this Vendor's inventory"""
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True    
        
        
    
