from swap_meet.item import Item
import uuid

class Decor(Item):  
    def __init__(self, id=uuid.uuid4().int, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def __str__(self):
        string = super().__str__() + f" It takes up a {self.width} by {self.length} sized space."
        return string