from swap_meet import item
import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        if id is not None and not isinstance(id, int):
            raise ValueError("id must be an integer")    
        self.id = id or int(uuid.uuid4())        
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
