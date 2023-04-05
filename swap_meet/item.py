from uuid import uuid4

class Item:
    def __init__(self, id=None):
        self.id = uuid4().int if id is None else id
    # use this in wave 5 (probably for all modules)

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return "Item"
    
