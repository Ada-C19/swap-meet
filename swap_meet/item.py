import uuid

class Item:
    def __init__(self,id = None,condition = 0):
        if id is None:
            id = uuid.uuid4().int
        self.id = id 
        self.condition = condition 
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition < 3:
            return "Item heavily used"
        elif self.condition < 5:
            return "Second-hand but almost like new"
        elif self.condition == 5:
            return "Brand-new item!"