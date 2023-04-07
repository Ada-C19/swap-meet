import uuid

class Item:
    def __init__(self, id= None, condition=0):
        if id is not None:
            self.id = uuid.uuid4()
        self.id = id or int(uuid.uuid4())
        self.condition = condition
        
    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 0:
            return "very bad"
        elif self.condition == 1:
            return "pretty bad"
        elif self.condition == 2:
            return "ehhhh, it'll do"
        elif self.condition == 3:
            return "pretty good"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 5:
            return "brand new"

    

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."



