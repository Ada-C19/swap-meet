# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, id=None, condition=0, age=0, type=None):
        super().__init__(id, condition, age)
        self.type = "Unknown" if type is None else type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."