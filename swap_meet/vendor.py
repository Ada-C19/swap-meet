from swap_meet.item import Item

# 1. create the Vendor class
class Vendor: 
    
    # 2. Vendor will have an attribute named inventory, 
    # which is an empty list by default
    def __init__(self, inventory=None):

        self.inventory =  inventory if inventory is not None else []
        
        

    # 3. Every instance of Vendor has an instance method named add, 
    # which takes in one item
    def add(self, added_item):
        self.added_item = added_item
            
        # 3a. This method adds the item to the inventory
        self.inventory.append(added_item)
        # 3b. This method returns the item that was added
        return added_item
        
    # 4. every instance of Vendor has an instance method named remove, 
    # which takes in one item
    def remove(self, removed_item):
        self.removed_item = removed_item
            
        # 4a. This method removes the matching item from the inventory
        if removed_item in self.inventory: 
            self.inventory.remove(removed_item)
            # 4b. This method returns the item that was removed
            return removed_item
        else:
            return False
        
    # instance method get_by_id 
        # This method takes one argument: an integer, 
        # representing an Item's id
    def get_by_id(self, id):
        
        
        for item in self.inventory:
            # This method returns the item 
            # with a matching id from the inventory
            if item.id == id:
                return item
            
            # If there is no matching item in the inventory, 
            # the method should explicitly return None
        return None
    
    # instance method named swap_items
    # takes 3 arguments
    # other_vendor, my_item, their item
    def swap_items(self, other_vendor, my_item, their_item):
        # self.other_vendor = other_vendor
        # self.my_item = my_item
        # self.their_item = their_item
        
        # if my item isn't in my inventory, OR if their item isn't in their inventory: 
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            #  then return False
            return False

        # removing  the item i have from my inventory
        self.inventory.remove(my_item)
        #  adding my item to their inventory 
        other_vendor.inventory.append(my_item)

        # removing the item they have from their inventory
        other_vendor.inventory.remove(their_item)
        
        # adding their item to my inventory
        self.inventory.append(their_item)
    
        return True
        

# wave 4 
# swap_first_item takes one argument, other_vendor
    def swap_first_item(self, other_vendor):
        
        # considers the first item in the instance's inventory: self.inventory[0]
        # and the first item in the friend's inventory: other_vendor.inventory[0]
        if len(self.inventory) == 0  or len(other_vendor.inventory)== 0:
            return False

        
        # adds first item from friends' inventory
        self.inventory.append(other_vendor.inventory[0])
        
        # remove first item from friend inventory
        other_vendor.inventory.remove(other_vendor.inventory[0])

        # adds the instance's first item
        other_vendor.inventory.append(self.inventory[0])


        # remove first item from your inventory
        self.inventory.remove(self.inventory[0])
                

        return True

    # wave 6 - SJ
    #  three instance methods: get_by_category, get_best_by_category, swap_best_by_category
    
    
    # one argument: a string, representing a category
    # list of objects in the inventory - self.inventory
    def  get_by_category(self, category):
        # self.inventory is a list
        new_list = []
        
        # if items in self.inventory match the category,
        # return the list
        for item in self.inventory:
            if category == item.get_category():
                new_list.append(item)
                
            # If there are no items in the inventory 
            # that match the category argument, 
            # the method returns an empty list
        return new_list
            

        

        
        
        # returns a list of objects in the inventory with that category
        return []    
    
    
    # get the item with the best condition in a certain category
    # one argument: a string that represents a category
    
    def  get_best_by_category(self, category):
        # loops through the inventory, for items w/ highest condition (5)
        #  AND the matching category
        
        # list of items that match the given category
        items_of_category = self.get_by_category(category)
        
        item_with_best_condition = None
        
        for item in items_of_category:
            
            # finding the highest, we can keep track 
            if item_with_best_condition == None:
                item_with_best_condition = item
            
            elif item.condition > item_with_best_condition.condition:
                item_with_best_condition = item
        return item_with_best_condition                
    
    
    
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
    
    
# wave 6- KV
# This method takes one argument:
#   a string, representing a category
# This method returns a list of objects in the inventory
#   with that category
# If there are no items in the `inventory` 
#   that match the category argument, 
# #   the method returns an empty list    
    # def get_by_category(self, category):
    #     filtered_categories = []
        
    #     for item in self.inventory:
    #         if item.get_category() == item:
    #             filtered_categories.append(item)
    #     return filtered_categories

# takes one argument:
#   a string that represents a category
# This method looks through the instance's `inventory` 
#   for the item with the highest `condition`
#   and matching `category`
# It returns this item
# If there are no items in the `inventory` that match the category, it returns `None`
# It returns a single item even
#   if there are duplicates 
#   (two or more of the same item with the same condition)        
    # def get_by_best_category(self, category):
    #     for item in self.category and condition:
    #         return item
    #     else:
    #         return None
    #         if item == 2:
    #             return inventory[0]