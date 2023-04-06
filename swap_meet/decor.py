import uuid


class Decor:

    def __init__(self, id=None, width=0, length=0, condition=0):
        if id:
            self.id = id
        else:
            self.id = int(uuid.uuid4())
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def condition_description(self):
        if self.condition == 0:
            return "cannot reuse"
        elif self.condition == 1:
            return "poor"
        elif self.condition == 2:
            return "heavily used"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "like-new"
        elif self.condition == 5:
            return "new"