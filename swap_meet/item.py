from uuid import uuid4

class Item:

    def __init__(self, id=0):
        self.id = id if id else uuid4().int
        
    def get_category(self):
        return self.__class__.__name__
    

a = Item()
print(a.get_category())