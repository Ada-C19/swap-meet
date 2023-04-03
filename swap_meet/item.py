# import uuid package
import uuid

class Item:
    # each Item will have an attribute, id -- which is a unique integer by default
    def __init__(self, id= None):
        
        # using UUID4 since UUID1 creates a UUID with the computer's network address 
        # UUID.int- returns the UUID as a 128-bit integer.
        # self.id = uuid.uuid4().int
        
        self.id = id if id is not None else uuid.uuid4().int
        # return id
        
    # Each item will have a function named get_category
    def get_category(self): 
        return __class__.__name__        