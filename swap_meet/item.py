import uuid
import math

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id and not isinstance(id,int):
            raise TypeError("id must be an integer")
        
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age
            
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        condition = math.ceil(self.condition)
        DESCRIPTIONS = {
            0: "Throw it away!",
            1: "It's seen better days",
            2: "Meh",
            3: "It's alright",
            4: "Pretty good!",
            5: "Practically new"
        }
        return DESCRIPTIONS.get(condition, "Invalid condition rating.")
        