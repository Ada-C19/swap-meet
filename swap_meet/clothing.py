import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown", condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return (f"An object of type Clothing with id {self.id}. "
                f"It is made from {self.fabric} fabric.")
    