import uuid
class Item:
    def __init__(self,id = None):
        id = uuid.uuid4().int if id is None else id
        self.id = id
    
    def get_category(self):
        return "Item"
   
        
