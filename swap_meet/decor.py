from swap_meet.item import Item


class Decor(Item):
        
    def __init__(self, id, width=0, length=0, condition=0):
        super().__init__(id, condition)
        self.id = id
        self.width = width
        self.length = length

    def __str__(self):
        category_id_description = super().__str__()
        return f"{category_id_description} It takes up a {self.width} by {self.length} sized space."