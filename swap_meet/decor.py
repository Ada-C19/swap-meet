# import uuid 
from swap_meet.item import Item


class Decor(Item):
    def __init__(self, id = None, width = 0, length = 0, condition = 0): 
        super().__init__(id, condition)
        # self.id = id
        self.width = width
        self.length = length
        # self.condition = condition

        # if id == None: 
        #     self.id = uuid.uuid4().int
        # else: 
        #     self.id

    # def get_category(self): 
    #     return self.__class__.__name__

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    # def condition_description(self): 
    #     if self.condition <= 1: 
    #         return "You probably want a glove for this one..."
    #     elif self.condition <= 3: 
    #         return "It's aight."
    #     elif self.condition <= 5: 
    #         return "Practically brand new, almost."
