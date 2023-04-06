import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
    def get_category(self):
        return Item.__name__

