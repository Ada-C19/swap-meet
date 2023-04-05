import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if type(id) != int and id != None:
            raise TypeError("id must be an int")
        if not id:
            id = uuid.uuid4().int
        self.id = id
        if type(condition) != int and type(condition) != float and condition != None:
            raise TypeError("condition must be an int or a float")
        self.condition = condition
        if type(age) != int and type(age) != float and age != None:
            raise TypeError("age must be an int or a float")
        self.age = age 
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."    

    def condition_description(self):
        ratings = {0:"As Bad As It Gets", 1: "Problably Not Worth It", 2: "OK", 3: "Pretty Good", 4: "Like New", 5: "Brand New!"}
        return ratings[self.condition]
