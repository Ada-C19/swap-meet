import uuid

class Clothing:
    
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        id = uuid.uuid4().int if id is None else id
        self.id = id
        self.fabric = fabric

    def get_category(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        descriptions = ["heavily used", "fair","good","like new","never worn","new with tag"]
        return descriptions[self.condition]