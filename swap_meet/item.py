import uuid
class Item:
    def __init__(self, id=None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def __str__(self):
        my_string = f'{self.id}'
        return f"An object of type {self.get_category()} with id {my_string}."
    
    def get_category(self):
        return self.__class__.__name__
    
    