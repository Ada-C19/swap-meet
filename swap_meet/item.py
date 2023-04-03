import uuid

class Item:
    def __init__(self, id=uuid.uuid4().int):
        if type(id) != int:
            raise Exception("id must be an integer")
        self.id = id
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."    

