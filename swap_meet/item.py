import uuid 
class Item:
    def __init__(self, id = None, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age
    def get_category(self):
        return "Item"
    def tell_age(self):
        return f"The {self.get_category()} is {self.age} years old"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 5:
            return "This item is in mint condition"
        elif self.condition == 4:
            return "This item is in great condition"
        elif self.condition == 3:
            return "This item is in good condition"
        else:
            return "This item is not in good condition"

