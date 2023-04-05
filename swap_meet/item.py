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

        name = Item("name")

        return type(name).__name__


################# WAVE 3 ######################

    def __str__(self):
        return f"An object of type Item with id {self.id}." 