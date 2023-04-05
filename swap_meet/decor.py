import uuid
class Decor:
    def __init__(self, id=None, width=0, length=0, condition=0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.width = width
        self.length = length
        self.condition = condition
        
    def get_category(self):
        return "Decor"
    
    def __str__(self) -> str:
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def condition_description(self):
        decor_condition = ["mint", "like new", "gently used", "vintage", "heavily used", "worn"]
        for i in range(6):
            if i == self.condition:
                return decor_condition[i]
