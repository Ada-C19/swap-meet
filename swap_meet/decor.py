import uuid
from swap_meet.item import Item

# Wave 5- SJ
# 1. Decor class has 4 attributes, id, condition and width and length
# 1a. id attribute is by default a unique integer
# 1b. condition attribute by default, set to 0
# 1c. width and length attributes by default are set to 0
# 1d. Decor class can inherit id and condition from Item class

class Decor(Item):

    def __init__(self, id = None, condition= 0, width = 0, length = 0):
        super().__init__(id, condition)  

        self.width = width if width is not 0 else width
        
        self.length = length if length is not 0 else length
        
        
    # W5- SJ
    # 2. Created instance method condition_description 
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
    # 3. Created an instance method that returns a string of the class name
    def get_category(self):
        return self.__class__.__name__
    
    # W5 - SJ
    # 5. Created an instance method that returns a string 
    # describing the dimenstions
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

