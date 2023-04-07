from .item import Item


class Clothing(Item):
    def __init__(self, id = None, age = 0.0, condition = 0.0, fabric = "Unknown"):
        super().__init__(id= id, age = age, condition = condition)
        self.fabric = fabric


    def __str__(self):
        parent_str = super().__str__()
        return (f'{parent_str} It is made from {self.fabric} fabric.')