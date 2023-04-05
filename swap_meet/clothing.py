import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id= None, fabric=None, condition= None):
        # super().__init___(id, condition)
        self.fabric = "Unknown" if fabric is None else fabric
    
        random_id = uuid.uuid4()
        self.id = int(random_id) if id is None else id

        self.condition = 0 if condition is None else condition

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."