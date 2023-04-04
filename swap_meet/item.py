import uuid

class Item:
    def __init__(self, id= None):
        if id is not None and not isinstance(id, int):
            self.id = uuid.uuid4()
        self.id = id or int(uuid.uuid4())
        
        

    def get_category(self):
        return "Item"
    



# class Vendor:
#    def __init__(self, inventory=None):
#        if inventory is None:
#            inventory = []
#        self.inventory = inventory



