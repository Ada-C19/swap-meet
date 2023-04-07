import uuid
from swap_meet.item import Item


class Clothing:
    def __init__(self, id = None, fabric = None, condition = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        
        if fabric is None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric
            
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
        
    def get_category(self):
        return Clothing.__name__
    
    def __str__(self):
        id_value = self.id
        fabric_value = self.fabric
        return f"An object of type Clothing with id {id_value}. It is made from {fabric_value} fabric."
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            return "fair"
        elif 1 <= self.condition < 2:
            return "good"
        elif 2 <= self.condition < 3:
            return "excellent"
        elif 3 <= self.condition < 4:
            return "near-mint"
        elif 4 <= self.condition <= 5:
            return "new"
        

    