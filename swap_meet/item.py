import uuid
# from swap_meet.vendor import Vendor

class Item:
    def __init__(self,id=0, category="Item"): 
    #    self.id = int(uuid.uuid4()) if id == 0 else self.id = id         #if id > 0:
        if id == 0:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.category = category
    def get_category(self):
        #item = Item(id)
        #return item.__class__.__name__
        return self.category
    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."