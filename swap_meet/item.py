import uuid

class Item:
    def __init__(self, id = None):
        self.id = uuid.uuid4().int if id is None else id
        
    def get_category(self):
        # return "Item"
        return (f"{self.__class__.__name__}")
    
    def get_by_id(self):
        
