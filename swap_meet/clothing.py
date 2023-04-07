from .item import Item

class Clothing(Item):
    
    def __init__(self, age=0, id=None, condition=0, fabric="Unknown"):
        super().__init__(age, id, condition)
        self.fabric = fabric
    
    
    def get_category(self):
        return "Clothing"
    

    def __str__(self):
        line1 = super().__str__()
        line2 = f"It is made from {self.fabric} fabric."

        return " ".join((line1, line2))

        