import uuid
from swap_meet.item import Item


class Electronics:
    def __init__(self, id = None, type = None, condition = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
            
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
            
    def get_category(self):
        return Electronics.__name__
    
    def __str__(self):
        id_value = self.id
        type_value = self.type
        return f"An object of type Electronics with id {id_value}. This is a {type_value} device."
    
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
