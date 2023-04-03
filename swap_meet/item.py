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

    