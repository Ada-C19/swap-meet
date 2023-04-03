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
<<<<<<< HEAD
 

# instantiate a list and optionally pass in a list with keyword arg named inventory
# vendor_example = Vendor(inventory=[])   


    
=======

    def get_by_id(self, item_id):
        # for each item in my inventory
        for item_id in self.inventory:
            # if id in question matches any item_id i have,
            if item_id.id == item_id:
        # return item with matching id from inventory
                return item_id
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
        return False
>>>>>>> 4098a72ea9ff2d714975a83002040391cab5de65



