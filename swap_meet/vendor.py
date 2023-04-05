# import uuid
####################### WAVE 1 #############################

# do I need this??????
# from swap_meet.item import Item

# import swap_meet/item.py

class Vendor:
    # inventory is an empty list
    def __init__(self, inventory=None):

        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if item:
            self.inventory.append(item)
            return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
            # return self.inventory


####################### WAVE 2 #############################
    def get_by_id(self, id): 

        for item in self.inventory:
            if id == item.id:
                return item
        
        return None
    

################### WAVE 3 ########################
    def swap_items(self, other_vendor, my_item, their_item):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True 
    
################### WAVE 4 #############################

    def swap_first_item(self, other_vendor):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        




        

        

