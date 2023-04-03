import uuid

class Item:
    def __init__(self, id=uuid.uuid4().int, condition=0):
        if type(id) != int:
            raise Exception("id must be an integer")
        self.id = id
        self.condition = condition
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. "    

    def condition_description(self):
        ratings = {0:"As Bad As It Gets", 1: "Problably Not Worth It", 2: "OK", 3: "Pretty Good", 4: "Like New", 5: "Brand New!"}
        return ratings[self.condition]
