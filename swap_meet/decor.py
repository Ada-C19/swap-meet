import uuid

class Decor:
    def __init__(self, id=None, width=0, length=0, condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return (f"An object of type Decor with id {self.id}. "
                f"It takes up a {self.width} by {self.length} sized space.")
    