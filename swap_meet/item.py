import uuid

class Item:
    def __init__(self, id=None):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id 
        self.category = "Item"

    def get_category(self):
        return self.category
    
    

    def __str__(self):
        desc_string = f"An object of type {self.get_category()} with id {self.id}."
        return desc_string
        
