from .item import Item

class Clothing(Item):
    def __init__(self, year=None, id=None, fabric='Unknown', condition=0):
        super().__init__(year=year, id=id, condition=condition)
        if not isinstance(fabric, str):
            raise ValueError
        self.fabric = fabric 
    
    def __str__(self):
        return f'{super().__str__()} It is made from {self.fabric} fabric.'