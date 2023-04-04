from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = uuid4().int
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        condition = round(self.condition)
        
        if condition == 5:
            return "Brand New"
        if condition == 4:
            return "Like New"
        if condition == 3:
            return "Very Good"
        if condition == 2:
            return "Good"
        if condition == 1:
            return "Acceptable"
        else:
            return "As Is"