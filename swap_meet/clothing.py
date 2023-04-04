# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, fabric=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = "Unknown" if fabric is None else fabric
        self.condition = condition if condition is not None else condition

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."