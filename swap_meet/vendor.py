class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
        
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
        for item in self.inventory:
            if item.id == id:
                return item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item_avail = True if my_item in self.inventory else False
        their_item_avail = True if their_item in other_vendor.inventory else False

        if not my_item_avail or not their_item_avail:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)
        
        self.add(their_item)
        other_vendor.add(my_item)
        
        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]
        
        self.remove(self_first_item)
        self.add(other_first_item)
        
        other_vendor.remove(other_first_item)
        other_vendor.add(self_first_item)

        return True
        
# from item import Item

# item_a = Item()
# item_b = Item()
# item_c = Item()
# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# item_d = Item()
# item_e = Item()
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )

# result = fatimah.swap_first_item(jolie)

# assert len(fatimah.inventory) == 3
# assert item_a not in fatimah.inventory
# assert item_b in fatimah.inventory
# assert item_c in fatimah.inventory
# assert item_d in fatimah.inventory
# assert len(jolie.inventory) == 2
# assert item_d not in jolie.inventory
# assert item_e in jolie.inventory
# assert item_a in jolie.inventory
# assert result