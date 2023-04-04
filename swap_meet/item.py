import uuid

class Item:
    def __init__(self, id=None):
        if id is None:

            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def get_category(self):
        return self.__class__.__name__

#item has attribute named id
#use uuid to provide num
#UUID4 uses pseudo-random number generators to generate UUID.
#initialize instance of item with keyword id.
#get_category returns string hold name of class(object.__class__.__name__)

