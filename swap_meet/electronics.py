import builtins
from swap_meet.item import Item

class Electronics(Item):
    '''
    type should be a string containing a one or two-word description of the item
    id, condition, and age should all be ints or floats
    if id not specified, a unique id will be generated
    '''
    def __init__(self, type="Unknown", id=None, condition=0, age=0):
        super().__init__(id, condition, age)
        if builtins.type(type) != str:
            raise TypeError
        self.type = type

    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."

    def get_category(self):
        return "Electronics"
