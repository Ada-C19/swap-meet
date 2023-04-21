from .item import Item

class Electronics(Item):
    def __init__(self, year=None, id=None, type='Unknown', condition=0):
        super().__init__(year=year, id=id, condition=condition)
        if not isinstance(type, str):
            raise ValueError
        self.type = type
        
    def __str__(self):
        return f'{super().__str__()} This is a {self.type} device.'