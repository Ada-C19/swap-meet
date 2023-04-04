from .item import Item

class Clothing(Item):

    def __init__(self, id, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def get_category(self):
        return "Clothing"
    