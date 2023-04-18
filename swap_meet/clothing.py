from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric="Unknown", id=None, condition=0, age="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."