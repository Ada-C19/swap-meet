import uuid


class Item:
    def __init__(self, id=None, condition=0):
        self.id = id
        if id is None:
            self.id = int(uuid.uuid4())

        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        condition_rating = {
            0: "Unusable",
            1: "Heavily used",
            2: "Terrible",
            3: "Meh",
            4: "Decent",
            5: "Mint",
        }

        return condition_rating[self.condition]
