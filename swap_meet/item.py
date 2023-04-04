import uuid

class Item:
    
    def __init__(self, id=None):
        if not id:
            id=int(uuid.uuid4())
        self.id = id 
    

    def get_category(self):
        return (f"{self.__class__.__name__}")
    
    
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}.")
