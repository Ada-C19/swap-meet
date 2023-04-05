from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, fabric = "Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    def __str__(self):
        first_message = super().__str__()
        second_message = f"It is made from {self.fabric} fabric."
        return f"{first_message} {second_message}"