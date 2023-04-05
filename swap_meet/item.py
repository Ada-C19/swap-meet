import uuid

class Item:

    def __init__(self, id = None, condition=0):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        self.condition = condition
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0: 
            return "Scrap"
        if self.condition == 1: 
            return "Poor" 
        if self.condition == 2:
            return "Well loved!"
        if self.condition == 3: 
            return "Gently used"
        if self.condition == 4: 
            return "Like new"
        if self.condition == 5: 
            return "Mint condition"


        
    