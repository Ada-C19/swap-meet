from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric = "Unknown"):
        super().__init__(id= None)
        self.fabric = fabric
    
    # def get_category(self):
    #     super().get_category()
    
    def __str__(self):
        super().__str__()
        return f"It is made from {self.fabric} fabric."