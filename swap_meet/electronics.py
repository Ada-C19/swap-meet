from .item import Item

class Electronics(Item):

    def __init__(self, id = None, condition = 0.0, type = "Unknown", age = 0):
        super().__init__(id = id, condition = condition, age = age)
        self.type = type

    def __str__(self):
        parent_str = super().__str__()
        return (f'{parent_str} This is a {self.type} device.')
    
    