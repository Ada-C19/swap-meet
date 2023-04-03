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
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None


    def swap_items(self, other_vendor, my_item, their_item):
        # self.other_vendor = other_vendor
        self.my_item = my_item
        self.their_item = their_item

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
            
        return True
        

    def swap_first_item(self, other_vendor):
        other_vendor.inventory.remove(self.inventory[0])
        self.inventory.append(other_vendor.inventory[0])

        # other_vendor.inventory.remove(self.inventory[0])
        # self.inventory.append(other_vendor.inventory[0])


        





