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



        # first attempt
        # if id in self.inventory:
        #     return self.id
        # else:
        #     return None