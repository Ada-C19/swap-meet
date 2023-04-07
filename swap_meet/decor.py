import uuid


class Decor:
    def __init__(self, condition, width=0, length=0, id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return "Decor"

    def stringify(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def __str__(self):
        return self.stringify()
