from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=None):
        '''
        Constructor of Vendor class:
        Parameters:
            inventory - starts being an empty list if no argument is pased, represents all of the objects of the classs Item
              that self has and is willing to swap with other vendors
        '''

        #If no argument is passed for inventory it will initialize as an empty list
        if not inventory:
            inventory=[]
        self.inventory=inventory

    def add(self,new_item):
        '''
        input:
            self -
            new_item - object of the class item 
        output: 
            new_item - object of the class item 
            side effect: inventory will be updated with new_item added to the end of the list
        '''

        #Append new_item to the inventory parameter, return new_item

        self.inventory.append(new_item)
        return new_item
    
    def remove(self, old_item):
        '''
        input:
            self -
            old_item - object from the Item class that self will remove from its inventory list 
        output:
            old_item - if old_item is found in the inventory list it will be removed and returned 
                side effect- inventory will have the old_item removed 
            False - if old_item is not found inventory will not change
        '''
        #Validate if old_item is in inventory, remove the item if it is 

        if old_item in self.inventory:

            self.inventory.remove(old_item)
            return old_item
        
        #return False if old_item is not found in inventory 

        else:
            return False
        
    
    def get_by_id(self,items_id):
        '''
        input:
            self-
            items_id - int unique identifier for an object of the class Item 
        output:
            item - the object of the class Item that contains the id (items_id)
            None - if no item was found with the id (items_id)
        '''

        #Iterate over each item in inventory to check if it has the id (items_id)

        for item in self.inventory:
            if items_id == item.id: 
                return item
        return  
    

    
    def swap_items(self,other_vendor,my_item,others_item):
        '''
    input: 
        self -
        other_vendor - object of the same class vendor that self wants to trade with, 
        my_item - Item self wants to swap, 
        others_item- item other_vendor wants to swap
    output: 
        True - if self and othr_vendor have items that the other wants to swap
            Side effect- the inventory parameter for self and other_vendor is modified by having the new item and
                removing the old item
        False - if self or other_vendor does not have its corrsponding item in their inventory parameter
        '''

        #Check each of the vendors has the correct item to swap 

        if my_item in self.inventory and others_item in other_vendor.inventory:
            
            # remove the swap items from the inventory parameter for both vendors 
            self.inventory.remove(my_item)
            other_vendor.inventory.remove(others_item)
            
            #Append the swaped items to the inventory parameter for both vendors 
            self.inventory.append(others_item)
            other_vendor.inventory.append(my_item)
            
            #Return True confirming that the transaction has happened

            return True 
        
        # Return False if one of the vendors does not have the item
        return False


    
    def swap_first_item(self,other_vendor):
        '''
        input:
            self
            other_vendor - another object of the same class (vendor)
        output: 
            False - If either of the vendors have empty inventories 
            True - If both of the vendors have at least one item in their inventories 
                and a swap is done 
        '''

        #Validate if both of the vendors have items in their inventory parameters

        if len(self.inventory) and len (other_vendor.inventory):

            # assign a variable for the first item in the inventory list for self and other_vendor 
            # call the swap_items() method too swap items
            my_item=self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor,my_item,their_item)

            #Return True if the swap has ocurred

            return True 
        
        #Return False if either of the vendors inventory has no items in the list 

        return False 
    
    

    def get_by_category(self,category):
        '''
        input:
            self -
            category - str specifiying which type of item the inventory of self is going to be filtered by 
        output: 
            items_in_category - list of items that self has in its inventory under the category
                specified as an argument
        '''

        # Create empty list to add the items from the specified category
        items_in_category=[]

        #Iterate over each Item in the inventory of self, if the item has the specified category
        #   its appended to the new list 

        for item in self.inventory:

            if item.get_category() == category:
                items_in_category.append(item)

        return items_in_category
    

    

    def get_best_by_category(self,category):

        '''
        input:
            self
            category - str specific category of items that inventory will be filtered by 
        output:
            best_item - will return the item with the best rating in the specified category
            None - if there is no item with that specific category 
        '''

        # List of items in selfs inventory that have the specified category

        items_in_category = self.get_by_category(category)
        
        # If the len on the list with the specified item is empty return None

        if len(items_in_category)==0:
            return None
        
        #Get the first item on the list with self items filterd by category
        
        best_item = items_in_category[0]
        
        # Iterate over the filtered list of items 
        # If the conditon is better, save in the temporary variable
        # return the item with the best rating

        for item in items_in_category:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    


    def swap_best_by_category(self,other_vendor,my_priority, their_priority):
        '''
        input:
            self-
            other_vendor - object of Vendor class, with which self wants to swap items 
            my_priority - str category of Item that self wants to swap 
            their_priority - str category of Item that othe_vendor wants to swap 
        output:
            True - If self or vendor have items of the desired category, the highest rated item will be swaped 
                Side effect - inventory parameter of self and other_vendor will change by one item
            False - If self or vendor dont have an item of the desired category the swap will not go on 

        '''

        #Get the highest rated item from the inventory from the category desired by self and vendor
        
        my_swap= self.get_best_by_category(their_priority)
        their_swap = other_vendor.get_best_by_category(my_priority)

        #call method swap_items if my_swap and their_swap have an item these will be swaped
        # and True will be returned else False will be returned 
        
        return self.swap_items(other_vendor,my_swap,their_swap)

    




