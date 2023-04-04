import uuid

class Item:
    def __init__(self, id = None):
        
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return __class__.__name__

    
### Wave 2


# def get_category(self):
# return class name in a string

# import the [`uuid` package](https://docs.python.org/3/library/uuid.html) in `item.py` to create large ***unique*** numbers 
# `UUID` objects have [an attribute `int`](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) which allow us to access their value as an integer

