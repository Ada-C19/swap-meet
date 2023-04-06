import uuid

class Item:
    def __init__(self, id=None, condition=0.0):
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
        self.category = self.get_category()
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0.0:
            return "Mint condition"
        elif self.condition == 1.0:
            return "Good condition"
        elif self.condition == 2.0:
            return "Lightly used"
        elif self.condition == 3.0:
            return "Fair"
        elif self.condition == 4.0:
            return "Used"
        else:
            return "Don't bother"