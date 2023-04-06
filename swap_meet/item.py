from uuid import uuid4

class Item:
    def __init__(self, condition=0, id=None):
        self.id = id
        if not self.id:
            self.id = uuid4().int
        self.condition = condition

    def __str__(self) -> str:
        return f"An object of type {self.__class__.__name__} with id {self.id}"

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        if self.condition == 0:
            return "Quality Unknown"
        elif self.condition == 1.0:
            return "Very Bad Quality"
        elif self.condition == 2.0:
            return "Bad Quality"
        elif self.condition == 3.0:
            return "Okay Quality"
        elif self.condition == 4.0:
            return "Good Quality"
        elif self.condition == 5.0:
            return "Great Quality"
        else:
            raise ValueError("Invalid Condition")