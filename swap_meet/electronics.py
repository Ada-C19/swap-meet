import uuid
from swap_meet.item import Item

# need to change the syntax to allow Electronics class to inherit from Item class
# class ExampleChildClass(ExampleParentClass):
# Electronics class shares the same id and condition attributes as Item class
# Item constructor: def __init__(self, id=None, condition = 0):


class Electronics(Item):
    # Has an attribute id that is by default a unique integer
    # Has an attribute type that is by default the string "Unknown"
    # def __init__(self, id= None, type = "Unknown"):
    def __init__(self, id = None, condition = 0, type="Unknown", ):
        super().__init__(id, condition)  # will get Attribute Error without this

            
        # following a similar syntax for type as id
        self.type = type if type is not "Unknown" else type
        

        
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

