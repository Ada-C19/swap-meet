
class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False
    
    def add(self,element):
        self.inventory.append(element)
        return element
    
    def get_by_id(self, id):
        for element in self.inventory:
            if id == element.id:
                return element
        return None
    
    def swap_items(self, other_vendor, my_item, their_item,):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        return False


