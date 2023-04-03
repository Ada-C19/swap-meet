import uuid

class Item:

    # create attribute called 'id': unique integer by default
    # generate numbers with a package called uuid
    # use one of their functions to create large unique numbers meant to be used as identifiers
    # package returns uuid objects not integers but they do have an attribute int that we can assess the value as an integer
    # when initializing an instance of Item, pass in an integer with the keyword argument id to mannually set the items id.

    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid4().int
        self.id = id

    # each Item has a function called get_category: returns string holding name of class.
    
    def get_category(self):   
        return __class__.__name__
