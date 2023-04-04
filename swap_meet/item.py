import uuid

class Item():

    def __init__(self, id=None):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
    
    def get_category(self):
        return "Item"





