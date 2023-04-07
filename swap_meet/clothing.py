from swap_meet.item import Item

class Clothing(Item):
    '''
    fabric should be a string description of the fabric type
    id, condition, and age should all be ints or floats
    if id not specified, a unique id will be generated
    '''
    def __init__(self, fabric="Unknown", id=None, condition=0, age=0):
        super().__init__(id, condition, age)
        if type(fabric) != str:
            raise TypeError
        self.fabric = fabric

    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."

    def get_category(self):
        return "Clothing"