import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    def __str__(self):
        item_id = str(self.id)
        return f'An object of type {self.__class__.__name__} with id {item_id}.'

    def get_category(self):
        return self.__class__.__name__
    