import uuid


class Item:
    def __init__(self, id=None, condition=0, age=0):
        if not id:
            self.id = uuid.uuid1().int
        else:
            self.id = id
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        condition_dict = {
            0: "As-is",
            1: "Heavily Used",
            2: "Used",
            3: "Lightly Used",
            4: "Like New",
            5: "Brand New"
        }
        return condition_dict[self.condition]
