from swap_meet.item import Item
import uuid

class Decor(Item):  
    def __init__(self, id=None, condition=None, age=None, width=None, length=None):
        super().__init__(id, condition, age)
        if not width:
            width = 0
        self.width = width
        if not length:
            length = 0
        self.length = length

    def __str__(self):
        string = super().__str__() + f" It takes up a {self.width} by {self.length} sized space."
        return string