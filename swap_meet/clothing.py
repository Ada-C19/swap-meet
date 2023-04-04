from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id= None, fabric = "Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    # def get_category(self):
        # super().get_category()
    
    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."
