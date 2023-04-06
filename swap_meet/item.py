from uuid import uuid4

class Item:

    def __init__(self, id=0, condition= 0.0):
        self.id = id if id else uuid4().int
        self.condition = condition
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        cond_desc = ""
        
        if self.condition <= 1:
            cond_desc = "heavily used"
        elif self.condition >= 2 and self.condition <= 3:
            cond_desc = "used"
        elif self.condition > 3 and self.condition <= 5:
            cond_desc = "as new"
                
        return cond_desc
        