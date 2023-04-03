import uuid

class Item:
    def __init__(self, id = None):
        '''
        If id does not exist, assign unique id with uuid
        Otherwise, self.id = id
        '''
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
    
    # Function named `get_category` will return a string holding the name of the class
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return "An object of type Item with id {}.".format(self.id)