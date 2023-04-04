class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
        if self.inventory == None: 
            self.inventory = []
        else: 
            self.inventory 

    # adds single item to inventory and returns item added
    def add(self, item):  
        self.inventory.append(item)
        return item
    
    # removes single item from invetory, returns item removed | if not matching item in inventory, method should return False
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        return False


# instantiate a list and optionally pass in a list with keyword arg named inventory
# vendor_example = Vendor(inventory=[])   

    def get_by_id(self, item_id):
        # for each item in my inventory
        for item_instance in self.inventory:
            # if item_id in question matches any item_instance have,
            if item_instance.id == item_id:
                # return item with matching id from inventory
                return item_instance
            # if no matching item, then return None
        return None  
        

    def swap_items(self, other_vendor, my_item, their_item):
        # if i have item to give and they have their item to give 
        if my_item in self.inventory and their_item in other_vendor.inventory:
            # remove item from my list to...
            self.remove(my_item)
            # add to the other vendor's list then...
            other_vendor.add(my_item)
            # removes their item to give from their list
            other_vendor.remove(their_item)
            # and adds their item to my list
            self.add(their_item)
            return True
        
    

    def swap_first_item(self, other_vendor): 
        # if the item is not in anyones inventory
        if not self.inventory or not other_vendor.inventory:
        # return false
            return False
        # get the first item of self.inventory
        my_first_item = self.inventory[0]
        # get the first item of other_vendor.inventory
        other_first_item = other_vendor.inventory[0]
        # remove first item from self
        self.remove(my_first_item)
        # remove first item from other 
        other_vendor.remove(other_first_item)
        # add eachother's items
        self.add(other_first_item)
        other_vendor.add(my_first_item)

        return True




