import uuid

class Item:
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int    
        self.id = id

    def __str__(self):
        category = self.get_category()
        starter_statement = f"An object of type {category} with id {self.id}."
        if category == "Item":
            return starter_statement
        if category == "Clothing":
            return starter_statement + f" It is made from {self.fabric} fabric."
        if category == "Decor":
            return starter_statement + f" It takes up a {self.width} by {self.length} sized space."
        if category == "Electronics":
            return starter_statement + f" This is a {self.type} device."

    def get_category(self):
        if isinstance(self, Item):
            return "Item"