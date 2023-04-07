import uuid
from swap_meet.item import Item


class Electronics(Item):
    # Define attributes for Electronics instances
    def __init__(self, id = None, type = None, condition = None): 
        # User inheritance logic to inherit certain attributes of Item class
        super().__init__(id, condition)   
        # If no value provided for type, attribute type takes on "Unknown"
        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
            
    def get_category(self):
        # Return class name "Electronics"
        return Electronics.__name__
    
    # Stringify Electronics instances
    def __str__(self):
        # Read id attribute
        id_value = self.id
        # Read type attribute
        type_value = self.type
        # Return expected string
        return f"An object of type Electronics with id {id_value}. This is a {type_value} device."
