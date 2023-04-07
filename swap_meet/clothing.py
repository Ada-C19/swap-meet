import uuid
from swap_meet.item import Item

# Wave 5- SJ
# 1. Clothing class has 3 attributes, id, condition and fabric
# 1a. id attribute is by default a unique integer
# 1b. condition attribute by default, set to 0
# 1c. fabric attribute is by default the string "Unknown"
# 1d. Clothing class can inherit id and condition from Item class
#     Clothing class shares the same id and condition attributes as Item class
#     Item constructor: def __init__(self, id=None, condition = 0):
#     class ExampleChildClass(ExampleParentClass):



class Clothing(Item):
    
    def __init__(self, id=None, condition = 0, fabric = "Unknown"):
        super().__init__(id, condition)
        
        self.fabric = fabric if fabric is not "Unknown" else fabric

        
    # W5 - SJ
    # 2. Created instance method get_category, returns class name
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
    # describing the fabric
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."