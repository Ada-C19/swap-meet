import uuid
class Item:
    
    def __init__(self, id=None, condition=0):
        self.id = id
        if id is None:
            self.id = int(uuid.uuid4())

        self.condition = condition 

    def get_category(self):
        return str(self.__class__.__name__)
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
