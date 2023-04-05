import uuid
from swap_meet.item import Item

# need to change the syntax to allow Decor class to inherit from Item class
# class ExampleChildClass(ExampleParentClass):
# Decor shares the same id and condition attributes as Item class
# Item constructor: def __init__(self, id=None, condition = 0):




class Decor(Item):

    # Has an attribute id that is by default a unique integer
    # Holds 2 integer attributes width and length
    # both of these values should be 0 by default
    def __init__(self, id = None, condition= 0, width = 0, length = 0):
        super().__init__(id, condition)  # will get Attribute Error without this

                
        # following a similar syntax for width as id
        self.width = width if width is not 0 else width
        
        # following a similar syntax for length as id
        self.length = length if length is not 0 else length
        
        
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


        
    # Has a function get_category that returns "Decor"
    def get_category(self):
        return self.__class__.__name__
    
    # Has a stringify method that returns 
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."


