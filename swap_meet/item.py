import uuid
# from swap_meet.vendor import Vendor

class Item:
    def __init__(self,id=0): 
    #    self.id = int(uuid.uuid4()) if id == 0 else self.id = id         #if id > 0:
        if id == 0:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
    
    def get_category(self):
        item = Item()
        return item.__class__.__name__
    