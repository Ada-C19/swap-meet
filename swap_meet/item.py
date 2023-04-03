import uuid

class Item:
    def __init__(self, id=None):
        self.id = id if id != None else uuid.uuid4().int
        self.name = "Item"

    def get_category(self):
        return self.name