class Vendor():
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        

    def add(self, item):        
        inventory = self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        inventory = self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        other_vendor.inventory
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.remove(their_item)
        self.inventory.append(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        my_first = ""
        their_first = "" 
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            my_first = self.inventory.pop(0)
            other_vendor.inventory.append(my_first)

            their_first = other_vendor.inventory.pop(0)
            self.inventory.append(their_first)                   
        return True