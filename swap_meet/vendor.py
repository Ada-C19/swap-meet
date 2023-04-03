#   In Wave 1 we will create the Vendor class.
class Vendor:
    
        # Each Vendor will have an attribute named inventory, which is an empty list by default
        # When we instantiate an instance of Vendor, we can optionally pass in a list with the 
                    # keyword argument inventory
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    # Every instance of Vendor has an instance method named add, which takes in one item
    # This method adds the item to the inventory
    def add(self, item):
        self.inventory.append(item)
        # This method returns the item that was added
        return item

    # Similarly, every instance of Vendor has an instance method named remove, 
    # which takes in one item
    # This method removes the matching item from the inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            # This method returns the item that was removed
            return item
        else:
        # If there is no matching item in the inventory, 
        # the method should return False
            return False
        
# In Wave 2 we will create the Item class and the Vendor class'
#  get_by_id method.
   #def get_by_id():




#Each Item will have a function named get_category, which will return
#  a string holding the name of the class

#Instances of Vendor have an instance method named get_by_id

# This method takes one argument: an integer, representing an Item's id
# This method returns the item with a matching id from the inventory
# If there is no matching item in the inventory, the method should 
# explicitly return None

        


















