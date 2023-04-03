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