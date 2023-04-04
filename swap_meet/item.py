import uuid


class Item:
    def __init__(self, id=None):
        random_id = uuid.uuid1().int
        self.id = random_id if id is None else id

    def get_category(self):
        return "Item"
