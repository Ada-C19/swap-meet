import uuid


class Electronics:

    def __init__(self, id=None, type="Unknown", condition=0):
        if id:
            self.id = id
        else:
            self.id = int(uuid.uuid4())
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

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