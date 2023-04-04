import uuid
class Decor:
    def __init__(self, id = None, width = 0, length = 0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.width = width
        self.length = length

    def get_category(self):
        if isinstance(self, Decor):
            item_type = "Decor" 
        return item_type    
    
    def __str__(self):
        statement = "An object of type Decor with id " + str(self.id) + ". ""\nIt takes up a " + self.width + " by " + self.length + " sized space."
        print(str(self.id))
        print(statement)
        return statement