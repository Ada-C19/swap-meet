import uuid

class Decor:

    # Has an attribute id that is by default a unique integer
    # Holds 2 integer attributes width and length
    #   both ofthese values should be 0 by default
    def __init__(self, id = None, width = 0, length = 0):
        
        # using UUID4 since UUID1 creates a UUID with the computer's network address 
        # UUID.int- returns the UUID as a 128-bit integer.
        # self.id = uuid.uuid4().int
        self.id =  id if id is not None else uuid.uuid4().int
        
        # following a similar syntax for width as id
        self.width = width if width is not 0 else width
        
        # following a similar syntax for length as id
        self.length = length if length is not 0 else length
        
    # Has a function get_category that returns "Decor"
    def get_category(self):
        return self.__class__.__name__
    
    # Has a stringify method that returns 
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."


