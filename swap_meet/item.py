import uuid

class Item:
    def __init__(self, id = None):
        # setting id to be an optional argument
        # passing in large random int if no id being passed by user
        # allowing id to be overwritten if id being passed by user
        if id is None:
            id = uuid.uuid4().int
        self.id = id
    
    def get_category(self):
        # returns any objects name
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    
