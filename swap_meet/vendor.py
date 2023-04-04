# In Wave 1 we will create the Vendor class.
#     There is a module (file) named vendor.py inside of the swap_meet package (folder)
#     Inside this module, there is a class named Vendor
#     When we instantiate an instance of Vendor, we can optionally pass in a list with the keyword argument inventory
#     Every instance of Vendor has an instance method named add, which takes in one item
#     Similarly, every instance of Vendor has an instance method named remove, which takes in one item

class Vendor:

    # def add_to_list_ok(word, word_list=None):
    # word_list = word_list if word_list is not None else []
    # word_list.append(word)
    # return word_list

#     Each Vendor will have an attribute named inventory, which is an empty list by default
    def __init__(self,inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
#     This method adds the item to the inventory
        self.inventory.append(item)
#     This method returns the item that was added
        return item
    
    def remove(self, item):
#     If there is no matching item in the inventory, the method should return False
        if item not in self.inventory:
            return False 
#     This method removes the matching item from the inventory
        self.inventory.remove(item)
#     This method returns the item that was removed
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        elif my_item not in other_vendor.inventory and their_item not in self.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
    
# Wave 4

# In Wave 4 we will write one method, swap_first_item.

# Instances of Vendor have an instance method named swap_first_item

# It takes one argument: an instance of another Vendor (other_vendor), representing the friend that the vendor is swapping with

#This method considers the first item in the instance's inventory, and the first item in the friend's inventory

#  It removes the first item from its inventory, and adds the friend's first item

# It removes the first item from the friend's inventory, and adds the instances first item

#  It returns True

#  If either itself or the friend have an empty inventory, the method returns False
