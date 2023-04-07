from swap_meet.item import Item

# Wave 1- SJ
# 1. created the Vendor class
# 2. one attribute named inventory, empty list by default

class Vendor: 
    
    def __init__(self, inventory=None):
        self.inventory =  inventory if inventory is not None else []
    
    
    # Wave 1- SJ
    # 3. Created instance method named add, which takes in one item
    # 3a. This method adds an item to the inventory
    # 3b. This method returns the item that was added

    def add(self, added_item):
        self.added_item = added_item
            
        self.inventory.append(added_item)
        return added_item
        
        
    # Wave 1- SJ
    # 4. Created instance method named remove, which takes in one item
    # 4a. If a matching item is found, removes the item from the inventory
    # 4b. If no matching item is found, returns False

    def remove(self, removed_item):
        self.removed_item = removed_item
            
        if removed_item in self.inventory: 
            self.inventory.remove(removed_item)
            return removed_item
        else:
            return False
        
        
    # Wave 2- SJ
    # 5. Created an instance method that takes one argument, id an integer, 
    #    id represents an Item's id number in the inventory
    # 5a. This method returns the item from the inventory with the matching id 
    # 5b. If no match is found, the method returns None 
    
    def get_by_id(self, id):
        
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None
    
    
    # Wave 3- KV
    # 6. Created instance method named swap_items, takes 3 arguments
    # other_vendor, my_item, their item
    # 6a. if my item isn't in my inventory, OR if their item isn't in their inventory,
    # 6b. the return False
    # 6c. Otherwise, remove the item from my inventory
    # 6d. Add that item to their inventory 
    # 6e. Likewise, if the other vendors item is in their inventory, remove that item
    # 6f. Add that item to my inventory and retrun True

    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)

        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        
        self.inventory.append(their_item)
    
        return True
        

# Wave 4 - SJ
# 7. Created an instance method swap_first_item takes one argument, other_vendor
#    considers the first item in the instance's / self.inventory, 
#    and the first item in the friend's/ other_vendor.inventory
# 7a. if the inventory for either are 0, return False
# 7b. otherwise add that first item from their inventory to mine
# 7c. then remove that first item from their inventory 
# 7d. likewise, add the first item from my inventory to their inventory
# 7e. then remove my first item from my inventory
# 7f. return True

    def swap_first_item(self, other_vendor):
        
        if len(self.inventory) == 0  or len(other_vendor.inventory)== 0:
            return False

        self.inventory.append(other_vendor.inventory[0])
        
        other_vendor.inventory.remove(other_vendor.inventory[0])

        other_vendor.inventory.append(self.inventory[0])

        self.inventory.remove(self.inventory[0])
                
        return True


    # Wave 6 - SJ
    # Created instance methods: get_by_category
    # get_by_category takes in one argument: a string, representing a category
    # setting a new_list variable to contain the items we are searching for
    # using a for loop to search through the inventory,
    # if items in self.inventory match the category,
    # return the list
    # If there are no items in the inventory that match the category argument, 
    # the method returns an empty list


    def  get_by_category(self, category):
        new_list = []
        
        for item in self.inventory:
            if category == item.get_category():
                new_list.append(item)
                
        return new_list
    
    
    # Wave 6- SJ
    # Created instance method: get_best_by_category  
    # takes in one argument: a string that represents a category
    # items_of_category is a list of items that match the given category
    # loops through the inventory, for items w/ highest condition (5)
    # AND the matches the category
    # if there's only one item, return that item
    # else, returns the item with the best condition in a certain category

    
    def  get_best_by_category(self, category):
        
        items_of_category = self.get_by_category(category)
        
        item_with_best_condition = None
        
        for item in items_of_category:
            if item_with_best_condition == None:
                item_with_best_condition = item
            
            elif item.condition > item_with_best_condition.condition:
                item_with_best_condition = item
        return item_with_best_condition                  

    
    # @@ KV implimentation
    # def get_best_by_category(self, category):
    #     # call get_by_category method instance on self
    #     #  to get an items list with the specific argument passed in
    #     # save the instance of 'get_by_category' to the 'items' list
    #     items = self.get_by_category(category)
        
    #     # check if items list is empty
    #     if len(items) == 0:
    #         # if items list is empty return None
    #         return None
        
    #     # create best_item variable to represent a single item with the best condition
    #     # use lambda to get assert that item is the variable to iterate with and condition is the method instance to iterate through
    #     # use max() function to get the best_item result with the highest condition
    #     # max () by default will only return one item
    #     best_item = max(items, key=lambda item: item.condition)
        
    #     return best_item
    
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        # create item_they_want variable to represent the item that other_vendor wants
        # use get_best_by_category (with their_priority passed in as arugment) as an instance attirubute of self (vendor)
        item_they_want = self.get_best_by_category(their_priority)
        
        # create item_i_want variable to represnt the item that self (vendor) wants 
        # use get_best_by_category (with my_priority passed in as arugment) as an instance attirubute of other_vendor
        item_i_want = other_vendor.get_best_by_category(my_priority) 
        
        # create swapped_result variable to represent the item_they_want and the item_i_want
        # use swap_items instance method on self
        # pass arguments other_vendor, item_they_want, item_i_want into swap_items to pass in the correct items to swap and vendor to swap with
        swapped_result = self.swap_items(other_vendor, item_they_want, item_i_want)
    
        # swapped result will only take item_they_want and item_i_want as a single item
        # because swap_items uses the max () which by default returns a single item as the item with the max value
        return swapped_result




    # W6- SJ - Pseudo
    # swap the best item of certain categories with another Vendor
    # three arguments: other_vendor, my_priority, their_priority
    # other_vendor, which represents another Vendor instance to trade with
    # my_priority, which represents a category that the Vendor wants to receive
    # their_priority, which represents a category that other_vendor wants to receive
    
    def  swap_best_by_category(self):
        
        # the best item in my_inventory that MATCHES their_priority category
        # is swapped with 
        # the best item in other_vendor's inventory that matches my_priority
        # then returns True 
        
        # else if the vendor has no item that matches their_priority category, 
        #  no swap happens, 
        #  return False
        
        # else if the other_vendor has no item that matches my priority category,
        #  no swap happens
        # return False
        
        pass
