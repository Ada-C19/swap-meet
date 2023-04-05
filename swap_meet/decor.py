import uuid
class Decor:
    def __init__(self,id = None, width = 0, length = 0, condition = 0):
        self.id = id if id is not None else uuid.uuid4().int
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def condition_description(self):
        if self.condition == 0:
            return "thats too low"
        elif self.condition == 1:
            return "that's low"
        elif self.condition == 2:
            return "almost half way"
        elif self.condition == 3:
            return "past half way"
        elif self.condition == 4:
            return "so close"
        elif self.condition == 5:
            return "perfect"
    


