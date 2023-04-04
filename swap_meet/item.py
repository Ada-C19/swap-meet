import uuid
class Item:
    def __init__(self, id = None):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        print(self.id)

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return "Item"    
