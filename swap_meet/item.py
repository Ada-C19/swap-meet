from uuid import uuid4

class Item:
    def __init__(self, id=None):
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            id = uuid4()
            id = id.int
            self.id = id

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."