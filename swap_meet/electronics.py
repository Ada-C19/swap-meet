from .item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None, condition=0):
        super().__init__(id=id, condition=condition)
        self.type = 'Unknown' if type is None else type
        
    def __str__(self):
        return f'{super().__str__()} This is a {self.type} device.'
