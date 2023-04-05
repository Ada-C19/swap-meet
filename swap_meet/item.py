from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            self.id = uuid4().int
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        condition_guide = {5: "Brand New", 4: "Like New", 3: "Very Good", 2: "Good",
                         1: "Good", 0: "As Is"}
        
        return condition_guide[round(self.condition)]