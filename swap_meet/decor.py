import uuid
from swap_meet.item import Item

class Decor(Item):
    

    def __init__(self, id=None, width=0, length=0, condition= 0.0):
        self.id = id if id is not None else int(uuid.uuid4())
        self.width = width 
        self.length = length
        self.condition = condition
    

    def get_category(self):
        return "Decor"
    

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def condition_description(self):
        
        condition_dict = {
            0: "Horrible",
            1: "Damaged",
            2: "Average",
            3: "Good",
            4: "Great",
            5: "Mint"
        }

        return condition_dict[self.condition]