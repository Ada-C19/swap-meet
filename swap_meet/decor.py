import uuid
from swap_meet.item import Item


class Decor(Item):
    # Define attributes for Decor instances
    def __init__(self, id = None, width = None, length = None, condition = None): 
        # User inheritance logic to inherit certain attributes of Item class
        super().__init__(id, condition)   
        # If no value provided for width, attribute width takes on 0    
        if width is None:
            self.width = 0
        else:
            self.width = width
            
        # If no value provided for length, attribute length takes on 0    
        if length is None:
            self.length = 0
        else:
            self.length = length   
            
    def get_category(self):
        # Return class name "Decor"
        return Decor.__name__
    
    #Stringify Decor instances
    def __str__(self):
        # Read id attribute
        id_value = self.id
        # Read width attribute
        width_value = self.width
        # Read length attribute
        length_value = self.length
        # Return expected string
        return f"An object of type Decor with id {id_value}. It takes up a {width_value} by {length_value} sized space." 