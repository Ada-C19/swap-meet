import uuid

class Item:
    
    # item constructor 
    def __init__(self, id = None):
        if not id: 
            id = uuid.uuid4().int
        self.id = id
    
    # get by category method
    def get_category(self): 
        return "Item"
    
    