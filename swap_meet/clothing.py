import uuid
from .item import Item

class Clothing(Item):
    def __init__(self, id = None, condition = 0, fabric = "Unknown"):
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return (f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric.")