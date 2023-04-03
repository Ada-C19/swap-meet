import uuid
class Item:
    # randomized id and set it to an integer
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id
    # accessing the class name of self (item)
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return(f"An object of type Item with id {self.id}.")
    
