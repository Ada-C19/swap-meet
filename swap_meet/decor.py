import uuid
from swap_meet.item import Item


class Decor(Item):
    
    def __init__(self, condition=0, id=None, width=0, length=0):
        super().__init__(condition, id)
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
