import uuid
# from swap_meet.vendor import Vendor

class Item:
    def __init__(self, id = None):
        if id != None:
            self.id = id
        else:
            self.id = uuid.uuid4().int

    
    def get_category(self):
        class_name = "Item"
        # class_name = __class__.__name__
        return class_name

        
    
    


    
