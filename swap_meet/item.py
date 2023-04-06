# ######################## WAVE 2 #############################
import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition


    def get_category(self):

        return self.__class__.__name__


################# WAVE 3 ######################

    
    def __str__(self):

        return f"An object of type {self.get_category()} with id {self.id}."


################# WAVE 5 #####################

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