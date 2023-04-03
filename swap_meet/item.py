import uuid

class Item:
    def __init__(self, id=None):
        # If id is passed assign it to id
        # If not create a new id
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
    
    def get_category(self):
        # Holds the class name and returns it as a str
        return self.__class__.__name__
    
    # This method will return the type this class as a Str not as an "An object of type Item with id <id value>."
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    

    