from uuid import uuid4

class Item:

    def __init__(self, id=0):
        self.id = id if id else uuid4().int
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
