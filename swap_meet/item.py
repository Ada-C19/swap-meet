import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
    def get_category(self):
        return Item.__name__
    
    def __str__(self):
        item_id = self.id
        return f"An object of type Item with id {item_id}."
        
    
    

