import uuid

class Item:
    def __init__(self, id = None, condition=0):
        self.id = uuid.uuid1().int if id is None else id
        self.condition = condition
        
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition > 4:
            return "Great"
        elif self.condition > 1:
            return "Okay"
        else:
            return "Uh-oh"