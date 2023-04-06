from uuid import uuid4

class Decor:
    def __init__(self, id=None, width=0, length=0):
        self.id = id
        if self.id is None:
            self.id = uuid4().int
        self.width = width
        self.length = length

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def get_category(self):
        return self.__class__.__name__