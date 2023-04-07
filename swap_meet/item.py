import uuid
# from swap_meet import Vendor


class Item:
    def __init__(self, id=None, condition=0):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())
        self.conditon = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition == 0:
            return "very bad"
        elif self.condition == 1:
            return "bad"
        elif self.condition == 2:
            return "fair"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 5:
            return "great"

        return "not acceptable"
