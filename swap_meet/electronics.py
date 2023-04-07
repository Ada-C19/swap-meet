import uuid


class Electronics:
    def __init__(self, type="Unknown", id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.type = type
