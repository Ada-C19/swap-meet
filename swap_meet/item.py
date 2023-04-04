import uuid

class Item:

    def __init__(self, id= None):
        if not id: 
            id = uuid.uuid4().int
        self.id = id 
    
    def __str__(self): 
        return "An object of type Item with id "+(str(self.id))+"."
    
    def get_category(self):
        return self.__class__.__name__
    
    