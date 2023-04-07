import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0, fabric="Unknown", id=None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.fabric = fabric
        self.category = "Clothing"
        super().__init__(id, condition) 
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
