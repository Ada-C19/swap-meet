import uuid
class Item:
    def __init__(self, id = -1):
        if id == -1:
            self.id = uuid.uuid4().int
        else:
            self.id = id 

    def get_category(self):
        return "Item"
    

    