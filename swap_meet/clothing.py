from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        self.fabric = fabric
        super().__init__(id, condition)

    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."