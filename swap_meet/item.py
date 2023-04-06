import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        self.id = uuid.uuid1().int if id is None else id
        self.condition = condition

    def get_category(self):
        return __class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        condition = {
            0 : "Heavily used",
            1 : "Used",
            2 : "Average",
            3 : "Good",
            4 : "Great",
            5 : "Perfect"
        }
        return condition[self.condition]
