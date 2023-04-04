import uuid

class Item:
    def __init__(self, id = None, condition = 0, age = None):
        if type(age) is not int:
            self.age = 0
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 0:
            return "used - heavily used"
        elif self.condition == 1:
            return "used - acceptable"
        elif self.condition == 2:
            return "used - good"
        elif self.condition == 3:
            return "used - very good"
        elif self.condition == 4:
            return "used - like new"
        elif self.condition == 5:
            return "new"