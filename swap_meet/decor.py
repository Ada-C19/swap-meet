from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, length = 0):
        super().__init__(id =id, condition = condition)
        self.width = width
        self.length = length

    def __repr__(self):
        return super().__repr__() + f" It takes up a {self.width} by {self.length} sized space."
        