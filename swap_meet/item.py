import uuid


class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        condition = ["0/5", "1/5", "2/5", "3/5", "4/5", "5/5"]
        return condition[self.condition]
