from uuid import uuid1

class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition
        self.id = uuid1().int if id is None else id

    def condition_description(self):
        if self.condition == 0:
            return "This is in poor condition. Rating is zero. "
        elif self.condition == 1:
            return "Think twice. Rating is 1. "
        elif self.condition == 2:
            return "This is an ok item. Rating is 2."
        elif self.condition == 3:
            return "This is a solid product, not top of the line. Rating is 3."
        elif self.condition == 4:
            return " You found a good one. Rating is 4."
        elif self.condition == 5:
            return "This is the best product ever. Rating is 5."
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return f"{self.__class__.__name__}"