class Vendor:

    def __init__(self, inventory=None): # inventory = empty list. Optionally pass in Keyword argument inventory?
        if inventory is None: 
            inventory = []
        self.inventory = inventory

    def add(self, item):
        #  adds the item to the inventory
        self.inventory.append(item)
        # returns the item that was added
        return item
    
    def remove(self, item):
        # method removes the matching item from the inventory
        if item in self.inventory: 
            self.inventory.remove(item)
        # returns the item that was removed
            return item 
        #If there is no matching item in the inventory, the method should return False
        return False 
    
    def get_by_id(self, id):
        for item in self.inventory:
            #return the item with a matching if from the inventory
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # removes my_item from this Vendor's inventory
        self.remove(my_item)
        #  adds it to the friend's inventory
        other_vendor.add(my_item)
        # removes their_item from the other Vendor's inventory
        other_vendor.remove(their_item)
        # adds it to this Vendor's inventory
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False

        my_item = self.inventory[0] 
        their_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_item, their_item,)

        return True 
        