from uuid import uuid1

class Item:
    def __init__(self, id=None):
        self.id = uuid1().int if id is None else id

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return f"{self.__class__.__name__}"