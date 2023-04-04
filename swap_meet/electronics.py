import uuid

class Electronics:
    # Has an attribute id that is by default a unique integer
    # Has an attribute type that is by default the string "Unknown"
    # def __init__(self, id= None, type = "Unknown"):
    def __init__(self, id = None, type="Unknown", condition = 0):
        
        
        # using UUID4 since UUID1 creates a UUID with the computer's network address 
        # UUID.int- returns the UUID as a 128-bit integer.
        # self.id = uuid.uuid4().int
        self.id =  id if id is not None else uuid.uuid4().int
        
        # following a similar syntax for type as id
        self.type = type if type is not "Unknown" else type
        
        # following a similar syntax for condition as id
        self.condition = condition if condition is not 0 else condition

        
    # Has a function get_category that returns "Electronics"
    def get_category(self):
        return self.__class__.__name__
    
    # which should describe the condition in words based on the value, 
    # assuming they all range from 0 to 5.
    def condition_description(self):
        condition = self.condition
        
        if condition == 0:
            return "Get the gloves on"
        elif condition == 1:
            return "Poor"
        elif condition == 2:
            return "Used"
        elif condition == 3:
            return "Good condition"
        elif condition == 4:
            return "Gently used"
        else: 
            return "Just like new!"

    
    # Has a stringify method that returns 
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."


