from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=[]):
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
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        #if my item isn't in my inventory, 
        #or their item not in their inventory return false.
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        #remove my item, add their item.
        self.remove(my_item)
        self.add(their_item)
        #for other vendor, remove their item, and add mine.
        other_vendor.remove(their_item)
        other_vendor.add(my_item)

        return True

