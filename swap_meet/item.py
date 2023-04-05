import uuid


class Item:
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    def get_category(self, item):
        return item
