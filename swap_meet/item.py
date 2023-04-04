import uuid

class Item:
    def __init__(self):
        self.id = int(uuid.uuid4())
    
    def get_category(self):
        