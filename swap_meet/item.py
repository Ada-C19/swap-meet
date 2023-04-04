import uuid

class Item:
    def __init__(self, id = None):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
    def get_category(self):
        return str(self.__class__.__name__)
    
    def __str__(self):
        return (f"An object of type Item with id {self.id}.")
