import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid4()
            self.id = int(id)
        else:
            self.id = id


    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."