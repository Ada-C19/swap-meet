# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, id=None, width=0, length=0, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.width = width if width is not None else width
        self.length = length if length is not None else length
        self.condition = condition if condition is not None else condition
        self.age = age if age is not None else age

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."