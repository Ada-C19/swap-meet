import uuid
from swap_meet.item import Item


class Decor(Item):
    def __init__(self, id = None, width = None, length = None, condition = None): 
        super().__init__(id, condition)   
        if width is None:
            self.width = 0
        else:
            self.width = width
        
        if length is None:
            self.length = 0
        else:
            self.length = length   
            
    def get_category(self):
        return Decor.__name__
    
    def __str__(self):
        id_value = self.id
        width_value = self.width
        length_value = self.length
        return f"An object of type Decor with id {id_value}. It takes up a {width_value} by {length_value} sized space." 