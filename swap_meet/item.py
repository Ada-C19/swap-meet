import uuid

class Item:
    def __init__(self, id=None):
        self.id = int(uuid.uuid4()) if id is None else id

    def get_category(self):
        return f"{self.__class__.__name__}"