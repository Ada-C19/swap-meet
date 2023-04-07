import uuid
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0.0):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        if isinstance(self, Electronics):
            item_type = "Electronics" 
        return item_type

    def __str__(self):
        statement = f"An object of type Electronics with id " + str(self.id) + ". This is a " + self.type + " device."
        print(statement)
        return statement   
