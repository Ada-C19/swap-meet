from swap_meet import vendor
import uuid

class Item:
    def __init__(self, id=None):
        if id is not None and not isinstance(id, int):
            raise ValueError("id must be an integer")    
        self.id = id or int(uuid.uuid4())
    
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."   