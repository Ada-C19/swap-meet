import uuid

class Item:
    def __init__(self, id=None):
        self.id = id or uuid.uuid4().int 
        # int(uuid.uuid4()) we call the int() to make it into an int

    # Each Item will have a get_category() which will return a str holding the name of the class
    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f'An object of type Item with id {self.id}.'