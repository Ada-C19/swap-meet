from swap_meet.item import Item

class Decor(Item):
    def __init__(self, width=0, length=0, id=None, condition=0):
        self.width = width 
        self.length = length 
        super().__init__(id, condition)

    def __str__(self): 
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."
