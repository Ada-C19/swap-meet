import uuid

class Item:
    def __init__(self, id=None, condition=None, name=None):
        self.id = id if id else uuid.uuid4().int
        self.name = name if name else "Item"
        self.condition = condition if condition else 0

    def get_category(self):
        return self.name
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Get the gloves on"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Like New"
        else:
            return "New"