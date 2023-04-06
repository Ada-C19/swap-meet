import uuid

class Item:
    def __init__(self, id = None, condition = 0.0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.condition=condition
    
    def get_category(self):
        return str(self.__class__.__name__)
    
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}.")
    
    def condition_description(self):
        if self.condition > 4.5:
            return "lightly used"
        elif self.condition > 3.0:
            return "used"
        elif self.condition > 2.0:
            return "fair"
        else:
            return "heavily used"
        
        
