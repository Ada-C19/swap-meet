import uuid

class Item:
    def __init__(self, id=None, condition=None, age=None):
        #if type(id) != int:
            #raise TypeError("id must be an int")
        if not id:
            id = uuid.uuid4().int
        self.id = id
        if not condition:
            condition = 0
        self.condition = condition
        if not age:
            age = 0
        self.age = age
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."    

    def condition_description(self):
        ratings = {0:"As Bad As It Gets", 1: "Problably Not Worth It", 2: "OK", 3: "Pretty Good", 4: "Like New", 5: "Brand New!"}
        return ratings[self.condition]
