import uuid
class Item:
    
    def __init__(self, id=0):
        self.id = id
        if self.id == 0:
            self.id = int(uuid.uuid4())

    def get_category(self):
        return str(self.__class__.__name__)