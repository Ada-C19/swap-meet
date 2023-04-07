import uuid

# Wave 2- SJ
# 1. each Item will have an attribute, id -- which is a unique integer by default
# 2. import uuid
#    using UUID4 since UUID1 creates a UUID with the computer's network address 
#    UUID.int- returns the UUID as a 128-bit integer.
#    self.id = uuid.uuid4().int

# following a similar syntax for condition as id



class Item:
    
    def __init__(self, id=None, condition = 0):

        self.id =  id if id is not None else uuid.uuid4().int
        
        self.condition = condition if condition is not 0 else condition


    # Wave 2- SJ
    # 3. Created an instance method get_category
    # 3a. returns a string of the class name
    def get_category(self):
        return self.__class__.__name__
    
    
    # which should describe the condition in words based on the value, 
    # assuming they all range from 0 to 5.
    def condition_description(self):
        condition = self.condition
        
        if condition == 0:
            return "Held together by magic and prayer. All swaps final"
        elif condition == 1:
            return "Needs a fair amount of repair"
        elif condition == 2:
            return "Some wear and tear"
        elif condition == 3:
            return "Good condition"
        elif condition == 4:
            return "Very gently loved"
        else: 
            return "Just like new!"
        

    # Wave 3- KV
    # calling a string on a class instance
    def __str__(self):
        return f"An object of type Item with id {self.id}."