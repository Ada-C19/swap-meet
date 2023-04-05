import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown", condition=0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.type = type
        self.condition = condition
        
    def get_category(self):
        return "Electronics"
    
    def __str__(self) -> str:
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    def condition_description(self):
        electronics_condition = ["mint", "like new", "gently used", "vintage", "heavily used", "worn"]
        for i in range(6):
            if i == self.condition:
                return electronics_condition[i]
