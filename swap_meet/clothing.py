# create large unique numbers to the ids
import uuid
from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, condition=0, age=0, fabric=None):
        super().__init__(id, condition, age)
        self.fabric = "Unknown" if fabric is None else fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."