import uuid
from .item import Item

class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, length = 0):
        self.id = uuid.uuid4().int if id is None else id
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return (f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space.")