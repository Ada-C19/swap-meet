import uuid
from swap_meet.item import Item


class Clothing(Item):
    
    def __init__(self, condition=0, id=None, fabric="Unknown"):
        super().__init__(condition, id)
        self.fabric = fabric
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."
