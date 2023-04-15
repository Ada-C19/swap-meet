import uuid

#from item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory #each vendor will have an attribute named :inventory (an empty list)
        
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
        print(item)
        return item 
    
    def remove(self, item): 
        
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            print(item.id)
            print(id)
            if item.id == id:
                return item
        return None
        

    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in other_vendor.inventory: 
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True 
    # these functions will return uuid objects **(not int)**  

        




# def swap
#         if self.inventory(other_vendor) == None or self.inventory(my_item) == None:
#             return False
#         else:
#             #consider first item in instances inventory
#             #consider first item in friends inventory
#             #removes first item from this inventory andd adds it to friends
#             #
#             return True
    

# ---------------- WAVE 4 --------------------
# In Wave 4 we will write one method, swap_first_item.

# Instances of Vendor have an instance method named swap_first_item
# It takes one argument: an instance of another Vendor (other_vendor), representing the friend that the vendor is swapping with
# This method considers the first item in the instance's inventory, and the first item in the friend's inventory
# It removes the first item from its inventory, and adds the friend's first item
# It removes the first item from the friend's inventory, and adds the instances first item
# It returns True
# If either itself or the friend have an empty inventory, the method returns Fals
