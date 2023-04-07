import uuid

class Item:
    def __init__(self, id=None, condition = 0.0):
        if not id:
            id = uuid.uuid1().int
        self.id = id
        self.condition = condition
        self.category = self.get_category()

    def get_category(class_type):
        return class_type.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition < 1:
            condition_description = "junky"
        elif self.condition == 1 or self.condition < 2:
            condition_description = "worn"
        elif self.condition == 2 or self.condition < 3:
            condition_description = "average wear"
        elif self.condition == 3 or self.condition < 4:
            condition_description = "lightly used"
        elif self.condition == 4 or self.condition < 5:
            condition_description = "opened"
        elif self.condition >= 5:
            condition_description = "new"
        return condition_description