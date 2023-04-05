from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition = 0, fabric = None):
        super().__init__(id=id, condition = condition)

        if fabric is None:
            fabric = "Unknown"
        self.fabric = fabric

    def __repr__(self):
        return super().__repr__() + f" It is made from {self.fabric} fabric."
        