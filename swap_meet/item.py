# There is a module (file) named item.py inside of the swap_meet package 
# (folder)
import uuid
# Inside this module, there is a class named Item
class Item:
    

    def __init__(self, id=0):
        if id is 0:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__

