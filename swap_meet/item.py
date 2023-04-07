import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if not id and not isinstance(id, int):
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        conditions = {
            0: "This should not even be sold. Don't buy it.",
            1: "Are you sure you really want this...?",
            2: "Fair condition, but will require fixing up.",
            3: "Good condition.",
            4: "Great condition! Gently used for sure.",
            5: "Mint condition, item is in excellent shape!"
        }

        try:
            return conditions.get(round(self.condition))
        except KeyError:
            return "Not sure what this grade condition is...(º～º)"