from swap_meet.item import Item


class Clothing(Item):
    
    def __init__(self, id, fabric="Unknown"):
        super().__init__(id)
        self.id = id
        self.fabric = fabric

    def __str__(self):
        category_id_description = super().__str__()
        return f"{category_id_description} It is made from {self.fabric} fabric."
