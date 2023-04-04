class Vendor:
    # passing optional argument called inventory 
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    # method that adds item to inventory 
    def add(self, item):
        if item:
            self.inventory.append(item)
        return item 
    # method that removes item from inventory if in inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item 

    def get_by_id(self, id):
        # if item is in inventory and matches item id the return item
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
            # check if items are in their respective inventories
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        # add item to other inventory and remove it from original inventory 
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True
            
    def swap_first_item(self, other_vendor):
        pass
    
    # def swap_items(self, other_vendor, my_item, their_item):
    #     #from vendor inventory remove my_item and add to other_vendor inventory
    #     #if either vendor doesn't have item in inventory return False
    #     if my_item in self.inventory:
    #         self.inventory.remove(my_item)
    #         other_vendor.inventory.append(my_item)
    #         return True
    #     #from other_vendor inventory remove their_item and add to vendor inventory
    #     elif their_item in other_vendor.inventory:
    #         other_vendor.inventory.remove(their_item)
    #         self.inventory.append(their_item)
    #         return True
    #     else:
    #         return False
        

            
