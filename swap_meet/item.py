from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        # check if need to cast into str
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
