import uuid

class Item:
    def __init__(self, id=None, condition=0.0):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
    
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."

    def condition_description(self):
        if self.condition == 5.0:
            return "This item is a steal!"
        elif 4.0 <= self.condition < 5.0:
            return "Better than average!"
        elif 3.0 <= self.condition < 4.0:
            return "Pretty average"
        elif 2.0 <= self.condition < 3.0:
            return "Well loved"
        elif 1.0 <= self.condition < 2.0:
            return "Seen better days"
        else:
            return "Better off in the trash"