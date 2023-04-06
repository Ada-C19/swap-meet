from .item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric=None, condition=0):
        super().__init__(id=id, condition=condition)
        self.fabric = 'Unknown' if fabric is None else fabric
    
    def __str__(self):
        return f'{super().__str__()} It is made from {self.fabric} fabric.'