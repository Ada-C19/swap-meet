import uuid
import random

class Item:
    
    # create attribute called 'id': unique integer by default
    # generate numbers with a package called uuid
    # assign keyword arguments to None so they can be modified for each instance seperately

    def __init__(self, id = None, condition = None):

        # create our random id number

        if id == None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition if condition else 0

    # create instance method called get_category: return string that is name of class

    def get_category(self):   
        return __class__.__name__
    
    # create instance method to stringify (convert to string) an Item

    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'
    
    # create method called condition_description to describe items condition value
    # condition value ranges from 0 to 5
    # accounted for any float values

    def condition_description(self):

        if 0 <= self.condition < 1:
            return 'Can\'t say I recommend that choice.'
        elif 1 <= self.condition < 2:
            return 'Well, I guess this is somewhat better.'
        elif 2 <= self.condition < 3:
            return 'Alright, not a bad choice at all!'
        elif 3 <= self.condition < 4:
            return 'Yeah, this is quite nice.'
        elif 4 <= self.condition < 5:
            return 'Used, Like new.'
        else:
            return 'Brand new!'