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
        
    def get_by_category(self, category):
        # input : sting rep a category
        # output: list of objects in the inv with that catergory
        
        # create empty list to hold results 
        result = []
        # iterate over the inv to find the item that has category clothing 
        for item in self.inventory:
        # get first item and use items get_category method to get the cagtegory string
            if item.get_category() == category:
        # compare
                result.append(item)
                # print(result)
        # if the category matches then add it to list for the category 
        return result 

    def get_best_by_category(self, category):
    # input: a string representing a category
    # output: the item with the best condition in the category, or None if no such item exists
    
    # get a list of items in the category
        items_in_category = self.get_by_category(category)
    
    # if there are no items in the category, return None
        if not items_in_category:
            return None
    
    # find the item with the highest condition in the category
        best_item = items_in_category[0]
        for item in items_in_category:
            if item.condition > best_item.condition:
                best_item = item
        
        return best_item


    # def get_best_by_category(self, category):
    #     #input: a string rep a category
    #     #output: a single item(no duplicates)
    #     item_category = self.get_by_category(category) 
    #                     # [item_a, item_c, item_e]
    #     #iterate over list to find highest condition
    #     # return the item 
    #     # get the items condition and determine the highest
    #     best_category = ''
    #     best_condition = 0
    #     for item in item_category:
    #         if item.condition > best_condition:
    #             item = best_category 

    #     if object.get_category == condition.type:  

