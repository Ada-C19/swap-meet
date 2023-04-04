
class Vendor:
    
# Wave 01
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        # This method returns the item that was added
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            # This method returns the item that was removed
            return item
        else:

            return False


# Wave 02
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None



# Wave 03 -- do last assert with Allison
    def swap_items(self, other_vendor, my_item, their_item):
        #
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        
        return False

# Wave 04
        # have an instance method named swap_first_ite
        #takes one argument: an instance of another Vendor (other_vendor)
                # representing the friend that the vendor is swapping with
    def swap_first_item(self, other_vendor):
        # If either itself or the friend have an empty inventory, t
        # he method returns False
        if not self.inventory or not other_vendor.inventory:
            return False
        # method considers the first item in the instance's inventory, and the first item 
                # in the friend's inventory
        vendor_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]
        # If either itself or the friend have an empty inventory, 
        # the method returns False
        if not vendor_first_item or not other_vendor_first_item:
            return False
        # It removes the first item from its inventory, 
        # and adds the friend's first item
        self.inventory.remove(vendor_first_item)
        self.inventory.append(other_vendor_first_item)
        #It removes the first item from the friend's inventory, 
        #and adds the instances first item
        other_vendor.inventory.remove(other_vendor_first_item)
        other_vendor.inventory.append(vendor_first_item)
        return True












