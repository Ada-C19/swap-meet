import uuid

class Item:
    def __init__(self, id = None):
        if id != None:
            self.id = id
        else:
            self.id = int(uuid.uuid4())

    def get_category(self):
        return self.__class__.__name__
    
    


    