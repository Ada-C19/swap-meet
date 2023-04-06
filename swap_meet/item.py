# ######################## WAVE 2 #############################
import uuid

# # do I need this???????
# # from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, id=None, condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition



# each item has this function
    # def get_category(self, name=""):
    def get_category(self):

        return self.__class__.__name__

        #Item is hard coded needs to be dynamic
        # NEED TO USE THE FOLLOWING:
        # return self.__class__.__name__
        # name = Item("name") 


################# WAVE 3 ######################

    # make item dynamic with {} 
    # can I set variables for each unique f string (one for clothing, decor, elec)
    
    def __str__(self):

        return f"An object of type {self.get_category()} with id {self.id}."


################# WAVE 5 #####################

    # need to account for rounding floats
    def condition_description(self):


        condition_of_items_dict = {
            0: "You don't want to buy this!",
            1: "Poor",
            2: "Fair, used condition",
            3: "Good, used condition",
            4: "Excellent, used condition",
            5: "NWT"
        }


        return condition_of_items_dict[round(self.condition)]