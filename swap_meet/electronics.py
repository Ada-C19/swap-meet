import uuid
from .item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = 0, type = "Unknown"):
        self.id = uuid.uuid4().int if id is None else id
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return (f"An object of type Electronics with id {self.id}. This is a {self.type} device.")