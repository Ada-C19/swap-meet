# from swap_meet.vendor import Vendor
import uuid

class Item:
    
    # each Item will have an attribute, id -- which is a unique integer by default
    # alse has an attribute called condition, 
    # which can be optionally provided in the initializer. 
    def __init__(self, id=None, condition = 0):

        # using UUID4 since UUID1 creates a UUID with the computer's network address 
        # UUID.int- returns the UUID as a 128-bit integer.
        # self.id = uuid.uuid4().int
        self.id =  id if id is not None else uuid.uuid4().int
        
        # following a similar syntax for condition as id
        self.condition = condition if condition is not 0 else condition


    # Each item will have a function named get_category
    def get_category(self):
        return self.__class__.__name__
    
    # which should describe the condition in words based on the value, 
    # assuming they all range from 0 to 5.
    def condition_description(self):
        condition = self.condition
        
        if condition == 0:
            return "Held together by magic and prayer. All swaps final"
        elif condition == 1:
            return "Needs a fair amount of repair"
        elif condition == 2:
            return "Some wear and tear"
        elif condition == 3:
            return "Good condition"
        elif condition == 4:
            return "Very gently loved"
        else: 
            return "Just like new!"
        

    # Wave 3- KC
    # calling a string on a class instance
    def __str__(self):
        return f"An object of type Item with id {self.id}."