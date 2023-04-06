import uuid

class Item:

    def __init__(self, id = None, condition = 0.0, age=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition
        self.age = age
    
    def get_category(self):
        return self.__class__.__name__
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0.0: 
            return "Scrap"
        if self.condition == 1.0: 
            return "Poor" 
        if self.condition == 2.0:
            return "Well loved!"
        if self.condition == 3.0: 
            return "Gently used"
        if self.condition == 4.0: 
            return "Like new"
        if self.condition == 5.0: 
            return "Mint condition"
    


        
    