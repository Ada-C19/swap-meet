from swap_meet.item import Item
import uuid
from swap_meet.item import Item

# need to change the syntax to allow Clothing class to inherit from Item class
# class ExampleChildClass(ExampleParentClass):
# Clothing class shares the same id and condition attributes as Item class
# Item constructor: def __init__(self, id=None, condition = 0):





class Clothing(Item)(Item):
    # Has an attribute id that is by default a unique integer
    
    # Has an attribute fabric that is by default the string "Unknown"
    
    def __init__(self, id=None, condition = 0, fabric = "Unknown"):
        super().__init__(id, condition)  # will get Attribute Error without this
        
        # following a similar syntax for fabric as id
        #  eventually fabric values may be :
        # new_clothing = Clothing(1234, "Striped") ..."Cotton", or "Floral"
        self.fabric = fabric if fabric is not "Unknown" else fabric

        
    # Has a function get_category that returns "Clothing
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
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."