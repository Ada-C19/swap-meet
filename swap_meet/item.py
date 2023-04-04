import uuid

class Item:
    def __init__(self, id=None, name=None):
        self.id = id if id else uuid.uuid4().int
        self.name = name if name else "Item"

    def get_category(self):
        return self.name
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."