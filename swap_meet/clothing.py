import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown", condition=0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.fabric = fabric
        self.condition = condition
        
    def get_category(self):
        return "Clothing"
    
    def __str__(self) -> str:
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        clothing_condition = ["mint", "like new", "gently used", "vintage", "heavily used", "worn"]
        for i in range(6):
            if i == self.condition:
                return clothing_condition[i]