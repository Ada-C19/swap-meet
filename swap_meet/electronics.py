import uuid
from swap_meet.item import Item

# Wave 5- SJ
# 1. Created an electronics class, takes in 3 attributes
# id, condition and type
# id  attribute is by default a unique integer
# type attribute is by default the string "Unknown"

class Electronics(Item):
    def __init__(self, id = None, condition = 0, type="Unknown", ):
        super().__init__(id, condition)
            
        self.type = type if type is not "Unknown" else type
        

    # W5 - SJ
    # 2. Created an instance method that returns a string of the class name
    
    def get_category(self):
        return self.__class__.__name__
    
    # W5- SJ
    # 3. Created instance method condition_description 
    #    which should describe the condition in words based on the value, 
    #    assuming the condition ranges from 0 to 5, 
    #    returns a string to describe the condition
    
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

    
    # W5 - SJ
    # 4. Created an instance method that returns a string 
    # describing the device's type
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

