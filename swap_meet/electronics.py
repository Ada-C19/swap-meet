import uuid
from swap_meet.item import Item

class Electronics:
    def __init__(self,id = None, type = "Unknown", condition = 0):
        self.id = id if id is not None else uuid.uuid4().int
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
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