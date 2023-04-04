import uuid
from uuid import uuid4
class Item:
    def __init__(self, id = None):
        id = uuid.uuid4().int if id is None else id
        self.id = id

    def get_category(self):
        return self.__class__.__name__
    
prueba = Item()
prueba2 = Item()
print(type(prueba.id),prueba.id)
print(type(prueba2.id),prueba2.id)
#uuid.uuid4().int