class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        # print("ENTERING REMOVE FUNCTION")
        if item in self.inventory:
            # print()
            # print(self.inventory)
            self.inventory.remove(item)
            # print("AFTER REMOVING")
            # print(self.inventory)
            return item
        
        return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            print("MY_INVENTORY")
            print(self.inventory)
            print("OTHER_VENDORS_INVENTORY")
            print(other_vendor.inventory)
            # Remove my_item form this Vendor's inventor 
            item_1_to_swap = self.remove(my_item)
            # Add it to the friend's inventory
            other_vendor.add(item_1_to_swap)
            # Remove their_item from other Vendor's inventory
            item_2_to_swap = other_vendor.remove(their_item)
            # add it to this Vendor's inventory
            self.add(item_2_to_swap)
            print("MY_INVENTORY")
            print(self.inventory)
            print("OTHER_VENDORS_INVENTORY")
            print(other_vendor.inventory)
            return True
        # If item isn't in the inventory
        return False
