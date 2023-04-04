import uuid

class Item:
    def __init__(self, id=None):
        self.id = id or uuid.uuid4().int

    # Each Item will have a get_category() which will return a str holding the name of the class
    def get_category(self):
        return type(self).__name__