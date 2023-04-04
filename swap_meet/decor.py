import uuid
from swap_meet.item import Item

class Decor:
    def __init__(self, id = None, width = 0, length = 0, condition = 0.0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        if isinstance(self, Decor):
            item_type = "Decor" 
        return item_type    
    
    def __str__(self):
        statement = (f"An object of type Decor with id " + str(self.id) + ". "
        "It takes up a " + str(self.width) + " by " + str(self.length) + " sized space.")
        print(str(self.id))
        print(statement)
        return statement
    
    def condition_description(self):
        if self.condition == 5:
            result = "Top tier! If you don't cop this, I will!"
        elif self.condition <= 2.0:
            result = "Yeahhhh, I don't know about this one."
        elif self.condition < 4:
            result = "I mean, it's aiight."
        elif self.condition < 5:
            result = "A hot commodity!"
        return result 