import uuid
class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id 
        

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 0:
            return f"Heavily Used"
        elif self.condition == 1:
            return f"getting better"
        elif self.condition == 2:
            return f"ok"
        elif self.condition == 3:
            return f"oooh better"
        elif self.condition == 4:
            return f"good"
        elif self.condition == 5:
            return f"Greeeeaaat"
    

    