import uuid

class Item:
    def __init__(self, id = None):
        id = uuid.uuid4().int if id is None else id
        self.id = id

    def __repr__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return self.__class__.__name__
    


    
    


