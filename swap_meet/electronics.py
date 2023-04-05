from swap_meet.item import Item
import uuid

class Electronics(Item):
    def __init__(self, id=None, condition=None, age= None, type=None):
        super().__init__(id, condition, age)
        if not type:
            type = "Unknown"
        self.type = type

    def __str__(self):
        string = super().__str__() + f" This is a {self.type} device."
        return string
    
    
