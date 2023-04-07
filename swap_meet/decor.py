from .item import Item

class Decor(Item):
    def __init__(self, id = None, age = 0.0, condition = 0.0, width = 0, length = 0):
        super().__init__(id = id, age = age, condition = condition)
        self.width = width
        self.length = length


    def __str__(self):
        parent_str = super().__str__()
        return (f'{parent_str} It takes up a {self.width} by {self.length} sized space.')