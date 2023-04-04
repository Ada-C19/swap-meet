import uuid 

class Item:
    def __init__(self, id = None):
        self.id = id
        if id == None: 
            self.id = uuid.uuid4().int
        else: 
            self.id

    def get_category(self): 
        return self.__class__.__name__

    def __str__(self):
        # if we pass in an item, w
        return f"An object of type Item with id {self.id}."