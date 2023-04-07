import uuid


class Decor:
    def __init__(self, width=0, length=0, id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.width = width
        self.length = length
