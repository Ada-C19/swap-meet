import uuid
class Item:
    def __init__(self, id= None, condition=None):
        random_id = uuid.uuid4()
        self.id = int(random_id) if id is None else id
        self.condition = 0 if condition is None else condition

    def get_category(self):
        return self.__class__.__name__
    def condition_description(self):
        if self.condition == 0:
            return f"You probably want a glove for this one..."
        elif self.condition == 1:
            return f"Poor"
        elif self.condition == 2:
            return f"Fair"
        elif self.condition == 3:
            return f"Good"
        elif self.condition == 4:
            return f"Like New"
        elif self.condition == 5:
            return f"New"