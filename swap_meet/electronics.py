from uuid import uuid4

class Electronics:
    def __init__(self, id=None, type="Unknown"):
        self.type = type
        self.id = id
        if self.id is None:
            self.id = uuid4().int

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. This is a {self.type} device."

    def get_category(self):
        return self.__class__.__name__