
import uuid 

class Clothing:
    def __init__(self,id = None, fabric = "Unknown"):
        if not id:
            id = int(uuid.uuid4())
        self.id = id

        self.fabric = fabric

    def get_category(self):
        return (self.__class__.__name__)
    
    def __str__(self):
        return( f'An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric.')