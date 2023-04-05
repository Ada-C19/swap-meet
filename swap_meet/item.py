import uuid
from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self,id = None):
        self.id = id if id is not None else uuid.uuid4().int
    
    def get_category(self):
        return f"{self.__class__.__name__}"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
        

    
    
