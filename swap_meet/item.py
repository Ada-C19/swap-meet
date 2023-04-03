import uuid
class Item:
    def __init__(self,id = None):
        id = uuid.uuid4().int if id is None else id
        self.id = id
    
    def get_category(self):
        return "Item"
   
    def __str__(self):
        return f"An object of type Item with id {self.id}."
