import uuid

class Clothing:
    def __init__(self, id = None, fabric = "Unknown"):
        if not id:
            id = uuid.uuid1().int
        self.id = id
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."