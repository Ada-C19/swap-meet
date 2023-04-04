from uuid import uuid4

class Item:
    def __init__(self, id=None):
        self.id = uuid4().int if id is None else id

    def get_category(self):
        # check if need to cast into str
        return "Item"
    
