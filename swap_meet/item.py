import uuid


class Item:
    def __init__(self, id=None, condition=0, age=0):
        random_id = uuid.uuid1().int
        self.id = random_id if id is None else id
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        condition_dict = {
            0: "Worn Out",
            1: "Heavily Used",
            2: "Normaly Used",
            3: "Lightly Used",
            4: "Like New",
            5: "Brand New"
        }
        return condition_dict[self.condition]
