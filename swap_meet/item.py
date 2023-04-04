import uuid

class Item:
    def __init__(self, id = uuid.uuid4().int):
        self.id = id