from .item import Item


class Clothing(Item):
    def __init__(self, id=0, fabric = "Unknown"):
        super().__init__(id, category="Clothing")
        self.fabric = fabric
        # self.fabric = "Unknown" if fabric is None else fabric

    def __str__(self):
        item_descript = super().__str__()
        clothing_description = f'It is made from {self.fabric} fabric.'
        return f"{item_descript} {clothing_description}"