from uuid import uuid4

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        self.fabric = fabric
        self.id = id
        if self.id is None:
            self.id = uuid4().int

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."

    def get_category(self):
        return self.__class__.__name__