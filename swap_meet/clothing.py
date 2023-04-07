from .item import Item


class Clothing(Item):
    def __init__(self,id=0, category="Clothing", fabric = "Unknown", condition=0):
        super().__init__(id, category, condition)
        self.fabric = fabric

    def __str__(self):
        item_descript = super().__str__()
        clothing_description = f'It is made from {self.fabric} fabric.'
        return f"{item_descript} {clothing_description}"