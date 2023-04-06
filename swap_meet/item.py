import uuid

class Item:

    # create attribute called 'id': unique integer by default
    # generate numbers with a package called uuid
    # use one of their functions to create large unique numbers meant to be used as identifiers
    # package returns uuid objects not integers but they do have an attribute int that we can assess the value as an integer
    # when initializing an instance of Item, pass in an integer with the keyword argument id to mannually set the items id.

    def __init__(self, id = None, condition = None):
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition if condition else 0


    # each Item has a function called get_category: returns string holding name of class.

        
    # each Item has a function called get_category: returns string holding name of class.   
    
    def get_category(self):   
        return __class__.__name__
    
    # write method to stringify (convert to string) an Item using str() 
    # write method called swap items

    def __str__(self):
        return f'An object of type Item with id {self.id}.'
    
    def condition_description(self):

        if 0 <= self.condition < 1:
            return 'Can\'t recommend.'
        elif 1 <= self.condition < 2:
            return 'Guess this is somewhat better.'
        elif 2 <= self.condition < 3:
            return 'Alright, not a bad choice at all!'
        elif 3 <= self.condition < 4:
            return 'Nice'
        elif 4 <= self.condition < 5:
            return 'Like new!'
        else:
            return 'Actually brand new!'
        