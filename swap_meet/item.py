import uuid

class Item:
    def __init__(self, id=None):
        if not id:
            id = int(uuid.uuid4())
        self.id = id

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return 'An object of type Item with id ' + str(self.id) + '.'
