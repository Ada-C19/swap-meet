####################### WAVE 1 #############################

# do I need this??????
from swap_meet.item import Item

class Vendor:
    # inventory is an empty list
    def __init__(self, inventory=[]):
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


    # def get_by_id(self, id):    
    #     if id in self.inventory:
    #         return self.item
    #     else:
    #         return None