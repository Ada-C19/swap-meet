import uuid
class Clothing:
    def __init__(self, id = None, fabric = "Unknown"):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.fabric = fabric

    def get_category(self):
        if isinstance(self, Clothing):
            item_type = "Clothing" 
        return item_type
    
    def __str__(self):
        statement = f"An object of type Clothing with id " + str(self.id) + ". It is made from " + self.fabric + " fabric."
        print(statement)
        return statement