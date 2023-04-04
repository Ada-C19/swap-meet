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
    # other_vendor, my_item
    def swap_items(self, other_vendor, my_item, their_item):
        # self.other_vendor = other_vendor
        # self.my_item = my_item
        # self.their_item = their_item

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
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
        
        
        
        # other_vendor.inventory.remove(self.inventory[0])
        # self.inventory.append(other_vendor.inventory[0])


        





