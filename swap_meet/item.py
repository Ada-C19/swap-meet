import uuid

class Item:
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int    
        self.id = id

    def get_category(self, item):
        if isinstance(item, Item):
            return "Item"