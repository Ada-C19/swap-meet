import uuid
from .item import Item
class Clothing(Item):
    def __init__(self, id=uuid.uuid1().int, fabric="Unknown", condition=0):
        self.id = id
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return (f"An object of type Clothing with id {self.id}."
                f" It is made from {self.fabric} fabric.")