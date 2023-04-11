from swap_meet.item import Item

class Decor(Item):
    '''
    width and length should both be ints or floats
    id, condition, and age should all be ints or floats
    if id not specified, a unique id will be generated
    '''
    def __init__(self, width=0, length=0, id=None, condition=0, age=0):
        super().__init__(id, condition, age)
        valid_type = [int, float]
        if type(width) not in valid_type or type(length) not in valid_type:
            raise TypeError
        self.width = width
        self.length = length

    def __str__(self):
        return super().__str__() + f" It takes up a {self.width} by {self.length} sized space."

    def get_category(self):
        return "Decor"