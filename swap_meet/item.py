import uuid

class Item:
    def __init__(self, id=None):
        self.id = int(uuid.uuid4()) if id is None else id

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return f"{self.__class__.__name__}"
    
