import uuid

class Item:
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int    
        self.id = id

    def get_category(self):
        if isinstance(self, Item):
            return "Item"