
from .item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        first_line = super().__str__()
        return f"{first_line} It is made from {self.fabric} fabric."
    
    

