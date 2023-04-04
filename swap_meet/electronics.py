import uuid
from swap_meet.item import Item

class Electronics:
    def __init__(self, id = None, type = "Unknown", condition = 0.0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.type = type
        self.condition = condition

    def get_category(self):
        if isinstance(self, Electronics):
            item_type = "Electronics" 
        return item_type

    def __str__(self):
        statement = f"An object of type Electronics with id " + str(self.id) + ". This is a " + self.type + " device."
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

