from swap_meet.item import Item


class Clothing(Item):
    
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric
        self.category = "Clothing"

    def __str__(self):
        category_id_description = super().__str__()
        return f"{category_id_description} It is made from {self.fabric} fabric."
