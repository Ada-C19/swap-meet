from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0.0):
        super().__init__(id)
        self.width = width
        self.length = length
        self.condition = condition
    
    def __str__(self):
        category_message = super().__str__()
        return f"{category_message} It takes up a {self.width} by {self.length} sized space."
    