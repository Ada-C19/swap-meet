import uuid


class Item:
    def __init__(self, id=None, condition=0):
        if id:
            self.id = id
        else:
            self.id = int(uuid.uuid4())
        self.condition = condition

    def get_category(self):
        class_name = Item()
        return class_name.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

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
