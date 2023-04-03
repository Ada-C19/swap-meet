import uuid

class Item(object):
    def __init__(self, id=None):
        if not id:
            self.id = uuid.uuid1().int
        else:
            self.id = id

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."
