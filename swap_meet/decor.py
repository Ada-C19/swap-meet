from .item import Item

class Decor(Item):
    def __init__(self, year=None, id=None, width=0, length=0, condition=0):
        super().__init__(year=year, id=id, condition=condition)
        self.width = width if width==0 else float(width)
        self.length = length if length==0 else float(length)
        if width < 0 or length < 0:
            raise ValueError
        
    def __str__(self):
        return f'{super().__str__()} It takes up a {self.width} by {self.length} sized space.'