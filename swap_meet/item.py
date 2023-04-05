import uuid


class Item:
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = str(uuid.uuid4())
