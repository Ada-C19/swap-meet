# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, id=None, type=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.type = "Unknown" if type is None else type
        self.condition = condition if condition is not None else condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."