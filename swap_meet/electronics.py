import uuid


class Electronics:
    def __init__(self, type="Unknown", id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.type = type

    def get_category(self):
        return "Electronics"

    def stringify(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def __str__(self):
        return self.stringify()
