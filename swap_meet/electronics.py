import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown", condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.type = type
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return (f"An object of type Electronics with id {self.id}. "
                f"This is a {self.type} device.")
    