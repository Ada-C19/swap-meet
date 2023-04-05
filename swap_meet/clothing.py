from swap_meet.item import Item
import uuid

class Clothing(Item):
    def __init__(self, id=None, condition=None, age=None, fabric="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        string = super().__str__() + f" It is made from {self.fabric} fabric."
        return string