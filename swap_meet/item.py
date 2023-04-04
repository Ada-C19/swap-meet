import uuid
<<<<<<< HEAD
=======
# from swap_meet.vendor import Vendor
>>>>>>> aae142ac564416676da73b2104a2b05304ac9319

class Item:
    def __init__(self, id = None):
        if id != None:
            self.id = id
        else:
<<<<<<< HEAD
            self.id = int(uuid.uuid4())

    def get_category(self):
        return self.__class__.__name__
=======
            self.id = uuid.uuid4().int

    
    def get_category(self):
        class_name = "Item"
        # class_name = __class__.__name__
        return class_name

        
>>>>>>> aae142ac564416676da73b2104a2b05304ac9319
    
    


<<<<<<< HEAD
    
=======
    
>>>>>>> aae142ac564416676da73b2104a2b05304ac9319
