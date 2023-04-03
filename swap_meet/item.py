import swap_meet.vendor as Vendor
import uuid 

# We can use uuid.uuid4() which will return an object
# which will look like this - UUID('16fd2706-8baf-433b-82eb-8c7fada847da')
# We can then use an attribute to get the actual integer called 'int'

# Example: id = uuid.uuid4() | then: id_int = id.int


class Item:
    def __init__(self, id=None):
        if id == None: 
            self.id = uuid.uuid4().int
        else: 
            id = None

    def get_category(self): 
        return self.__class__.__name__
