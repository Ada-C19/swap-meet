import uuid

class Electronics:
    # Has an attribute id that is by default a unique integer
    # Has an attribute type that is by default the string "Unknown"
    # def __init__(self, id= None, type = "Unknown"):
    def __init__(self, id = None, type="Unknown"):
        
        
        # using UUID4 since UUID1 creates a UUID with the computer's network address 
        # UUID.int- returns the UUID as a 128-bit integer.
        # self.id = uuid.uuid4().int
        self.id =  id if id is not None else uuid.uuid4().int
        
        self.type = type if type is not "Unknown" else type
        
    # Has a function get_category that returns "Electronics"
    def get_category(self):
        return self.__class__.__name__
    
    # Has a stringify method that returns 
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."


