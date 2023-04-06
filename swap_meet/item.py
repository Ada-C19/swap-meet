# ######################## WAVE 2 #############################
import uuid

# # do I need this???????
# # from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int
        self.id = id



# each item has this function
    def get_category(self, name=""):

        return self.__class__.__name__

        #Item is hard coded needs to be dynamic
        # NEED TO USE THE FOLLOWING:
        # return self.__class__.__name__
        # name = Item("name") 




################# WAVE 3 ######################

    # make item dynamic with {} 
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}." 




        # return f"An object of type Item with id {self.id}." 