import uuid
from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, id = None, type = None, condition = None): 
        super().__init__(id, condition)      
        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
            
    def get_category(self):
        return Electronics.__name__
    
    def __str__(self):
        id_value = self.id
        type_value = self.type
        return f"An object of type Electronics with id {id_value}. This is a {type_value} device."
