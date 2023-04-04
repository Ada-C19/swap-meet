import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id == None:
            id = uuid.uuid4().int
        elif not isinstance(id, int):
            raise ValueError("id must be an integer")
        self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Wear a hazmat suit for pickup"
        elif self.condition == 1:
            return "Ask your Mom to come pick you up, you will be scared"
        elif self.condition == 2:
            return "This just needs some tender-lovin' care"
        elif self.condition == 3:
            return "Meh, it's okay, might need a wash"
        elif self.condition == 4:
            return "Good find, just one or two problems with this one"
        elif self.condition == 5:
            return "Perfect condition! Someone probably accidently gave this away, but I guess you got lucky"