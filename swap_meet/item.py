import uuid

class Item:
    # each item will have an attribute named id
    #initialize an instance of item optionally pass in an int
    def __init__(self, id=None):
        if id is None:
            # func provides unique numbers to be used to id
            # create a unique int
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        # return a string holding the name of the class 
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."