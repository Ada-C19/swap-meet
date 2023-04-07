import uuid
from swap_meet.item import Item


class Clothing(Item):
    # Define attributes for Clothing instances
    def __init__(self, id = None, fabric = None, condition = None): 
        # User inheritance logic to inherit certain attributes of Item class
        super().__init__(id, condition)   
        # If no value provided for fabric, attribute fabric takes on "Unknown"    
        if fabric is None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric
        
    def get_category(self):
        # Return class name "Clothing"
        return Clothing.__name__
    
    # Stringify Clothing instances
    def __str__(self):
        # Read id attribute
        id_value = self.id
        # Read fabric attribute
        fabric_value = self.fabric
        # Return expected string
        return f"An object of type Clothing with id {id_value}. It is made from {fabric_value} fabric."
        

    