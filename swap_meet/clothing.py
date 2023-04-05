from .item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric=None):
        super().__init__(id=id)
        self.fabric = 'Unknown' if fabric is None else fabric
    
    def __str__(self):
        return f'{super().__str__()} It is made from {self.fabric} fabric.'