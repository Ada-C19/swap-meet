import uuid

class Item:
    def __init__(self, id = None):
        # setting id to be an optional argument
        # passing in large random int if no id being passed by user
        # allowing id to be overwritten if id being passed by user
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def get_category(self):
        # returns any objects name
        return self.__class__.__name__
