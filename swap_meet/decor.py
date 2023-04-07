import uuid
from swap_meet.item import Item


class Decor:
    def __init__(self, id = None, width = None, length = None, condition = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
        if width is None:
            self.width = 0
        else:
            self.width = width
        
        if length is None:
            self.length = 0
        else:
            self.length = length   
            
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
            
    def get_category(self):
        return Decor.__name__
    
    def __str__(self):
        id_value = self.id
        width_value = self.width
        length_value = self.length
        return f"An object of type Decor with id {id_value}. It takes up a {width_value} by {length_value} sized space."
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            return "fair"
        elif 1 <= self.condition < 2:
            return "good"
        elif 2 <= self.condition < 3:
            return "excellent"
        elif 3 <= self.condition < 4:
            return "near-mint"
        elif 4 <= self.condition <= 5:
            return "new"