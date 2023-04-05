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

    """
    Wave 4

    In Wave 4 we will write one method, swap_first_item.
    This method considers the first item in the instance's inventory, and the first item in the friend's inventory
    """

    # Instances of Vendor have an instance method named swap_first_item
    # It takes one argument: an instance of another Vendor (other_vendor), representing the friend that the vendor is swapping with
    def swap_first_item(self, other_vendor):
        
        #  If either itself or the friend have an empty inventory, the method returns False
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        
        if their_first_item not in self.inventory:
            #  It removes the first item from its inventory, and adds the friend's first item
            self.add(their_first_item)
            other_vendor.add(my_first_item)
            # It removes the first item from the friend's inventory, and adds the instances first item
            other_vendor.remove(their_first_item)
            self.remove(my_first_item)
            #  It returns True
            return True


    """
    In Wave 6 we will write three methods, get_by_category, get_best_by_category, and swap_best_by_category.

        Vendor objects have an instance method named get_by_category
            This method takes one argument: a string, representing a category
            This method returns a list of objects in the inventory with that category
            If there are no items in the inventory that match the category argument, the method returns an empty list

        Vendors have a method named get_best_by_category, which will get the item with the best condition in a certain category
            It takes one argument: a string that represents a category
            This method looks through the instance's inventory for the item with the highest condition and matching category
                It returns this item
                If there are no items in the inventory that match the category, it returns None
                It returns a single item even if there are duplicates (two or more of the same item with the same condition)

    The remaining tests in wave 6 imply:

        Vendors have a method named swap_best_by_category, which will swap the best item of certain categories with another Vendor
            It takes in three arguments
                other_vendor, which represents another Vendor instance to trade with
                my_priority, which represents a category that the Vendor wants to receive
                their_priority, which represents a category that other_vendor wants to receive
            The best item in my inventory that matches their_priority category is swapped with the best item in other_vendor's inventory that matches my_priority
                It returns True
                If the Vendor has no item that matches their_priority category, swapping does not happen, and it returns False
                If other_vendor has no item that matches my_priority category, swapping does not happen, and it returns False

    """

    
    def get_by_category(self, category):
        items = []

        if category not in self.inventory:
            return []
        
        for item in self.inventory:
            if isinstance(item, category):
                items.append(item)
        
        return items
    # Vendors have a method named get_best_by_category, which will get the item with the best condition in a certain category
    #     It takes one argument: a string that represents a category
    #     This method looks through the instance's inventory for the item with the highest condition and matching category
    #         It returns this item
    #         If there are no items in the inventory that match the category, it returns None
    #         It returns a single item even if there are duplicates (two or more of the same item with the same condition)
    
def get_best_by_category(self, category):
   #pseudo code 

   # for all the items in self inventory. 
   # look at the items with matching categories 
   # so decor item, decor item, electornic item, electornic item, 
   # out of those matching items, return the item with the highest condition. 
   # return ONE item, no duplicates. 
    