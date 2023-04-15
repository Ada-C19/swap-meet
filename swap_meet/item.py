import uuid

class Item:
    def __init__(self, id=None):        
        print("id", id)
        #if id is not manually assigned
        if id == None:
            self.id = uuid.uuid4().int
        #if id is manually assigned
        else:
            self.id = id
        
        
    def get_category(self):
        return self.__class__.__name__
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."    

    