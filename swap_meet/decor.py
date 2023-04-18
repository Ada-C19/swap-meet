from swap_meet.item import Item

class Decor(Item):
    def __init__(self, width=0, length=0, id=None, condition=0, age="Unknown"):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length

    def __str__(self):
        message = f" It takes up a {self.width} by {self.length} sized space."
        return f"{super().__str__()}" + message
    
