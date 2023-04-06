# import uuid 
from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0): 
        super().__init__(id, condition)
        # self.id = id
        self.type = type
        # self.condition = condition

        # if id == None: 
        #     self.id = uuid.uuid4().int
        # else: 
        #     self.id
        

    # def get_category(self): 
    #     return self.__class__.__name__

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    # def condition_description(self): 
    #     if self.condition <= 1: 
    #         return "You probably want a glove for this one..."
    #     elif self.condition <= 3: 
    #         return "It's aight."
    #     elif self.condition <= 5: 
    #         return "Practically brand new, almost."
