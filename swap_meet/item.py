from uuid import uuid4

class Item:
    def __init__(self, id=None):
        self.id = id
        if not self.id:
            self.id = uuid4().int

    def __str__(self) -> str:
        return f"An object of type {self.__class__.__name__} with id {self.id}"

    def get_category(self):
        return self.__class__.__name__
