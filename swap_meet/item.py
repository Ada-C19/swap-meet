import uuid 
"""
Module that contains class Item with attributes id, condition and age. 
Id attribute is default None, if id is assigned must be non-negative integer. Otherwise, Invalid id error message is raised. 
Item instance method str() overrides str method to print category and id. 
"""
class Item:
    def __init__(self, id=None, condition=0.0, age=0):        
        if id:
            if isinstance(id, int) and id > 0:
                self.id = id
            else:
                raise ValueError(f"Invalid id: {id}")
        else:
            self.id = uuid.uuid4().int
        
        self.condition = condition
        self.age = age 

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        description = ""
        if self.condition >= 0 and self.condition <1:
            description = "This item should not even be allowed to be here."
        if self.condition >= 1 and self.condition <2:
            description = "This item has seen better days."
        if self.condition >= 3 and self.condition <4:  
            description = "This item is not the best but also not the worst"
        if self.condition >= 4 and self.condition <5:
            description = "This item is the best there is."

        return description