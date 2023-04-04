import uuid
from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, width = 0, length = 0, condition = 0.0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def get_category(self):
        if isinstance(self, Decor):
            return "Decor" 

    
    def __str__(self):
        statement = (f"An object of type Decor with id " + str(self.id) + ". "
        "It takes up a " + str(self.width) + " by " + str(self.length) + " sized space.")
        print(str(self.id))
        print(statement)
        return statement
    